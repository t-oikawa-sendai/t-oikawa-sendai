#!/usr/bin/env python3
"""Update public student-material history from a validated distributed date."""

import argparse
from datetime import date, datetime
from pathlib import Path
import re
import os
import tempfile
from zoneinfo import ZoneInfo


SUMMARY = "受講生向け教材の配布内容を更新しました。"
MATERIAL = "AI活用入門"
DETAIL_PREFIX = "- **教材の更新日・変更概要：** "
TABLE_HEADER = "| 更新日 | 教材 | 変更概要 |"
TABLE_SEPARATOR = "|---|---|---|"
ROW = re.compile(r"^\| (\d{4}-\d{2}-\d{2}) \| ([^|]+) \| ([^|]+) \|$")


def parse_date(value: str) -> date:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Expected YYYY-MM-DD")
    return date.fromisoformat(value)


def update_readme(content: str, distributed_date: str) -> str:
    new_date = parse_date(distributed_date)
    if new_date > datetime.now(ZoneInfo("Asia/Tokyo")).date():
        raise ValueError("Distributed date is in the future in Japan")
    lines = content.splitlines(keepends=True)
    ai_headings = [
        i for i, line in enumerate(lines) if line.startswith("### [AI活用入門（")
    ]
    if len(ai_headings) != 1:
        raise ValueError("Expected exactly one AI material section")
    section_start = ai_headings[0]
    section_end = next(
        (i for i in range(section_start + 1, len(lines)) if lines[i].strip() == "---"),
        None,
    )
    if section_end is None:
        raise ValueError("AI material section has no end")
    detail_indices = [
        i for i in range(section_start, section_end) if lines[i].startswith(DETAIL_PREFIX)
    ]
    if len(detail_indices) != 1:
        raise ValueError("Expected exactly one AI material update field")
    detail_index = detail_indices[0]
    detail_match = re.fullmatch(
        r"- \*\*教材の更新日・変更概要：\*\* (\d{4}-\d{2}-\d{2})。.*\n?",
        lines[detail_index],
    )
    if detail_match is None:
        raise ValueError("Malformed AI material update field")
    current_date = parse_date(detail_match.group(1))

    headers = [i for i, line in enumerate(lines) if line.rstrip("\n") == TABLE_HEADER]
    if len(headers) != 1:
        raise ValueError("Expected exactly one recent-updates table")
    start = headers[0]
    if start + 1 >= len(lines) or lines[start + 1].rstrip("\n") != TABLE_SEPARATOR:
        raise ValueError("Malformed recent-updates table separator")
    end = start + 2
    entries = []
    while end < len(lines) and lines[end].startswith("|"):
        match = ROW.fullmatch(lines[end].rstrip("\n"))
        if match is None:
            raise ValueError("Malformed recent-updates row")
        entries.append((parse_date(match.group(1)), match.group(2), match.group(3)))
        end += 1
    if len(entries) != 5 or entries != sorted(entries, key=lambda item: item[0], reverse=True):
        raise ValueError("Expected five date-descending recent updates")
    ai_dates = [day for day, material, _ in entries if material == MATERIAL]
    if ai_dates and max(ai_dates) != current_date:
        raise ValueError("AI material field and history do not agree")
    # The latest AI update can legitimately fall outside the five visible rows.
    # Equal dates are also allowed: the table has no time-of-day ordering.
    if not ai_dates and current_date > entries[-1][0]:
        raise ValueError("AI material field and history do not agree")

    # Repeated or delayed dispatches must preserve an existing same-day summary.
    if new_date <= current_date:
        return content

    entries.append((new_date, MATERIAL, SUMMARY))
    entries.sort(key=lambda item: item[0], reverse=True)
    entries = entries[:5]
    lines[detail_index] = f"{DETAIL_PREFIX}{distributed_date}。{SUMMARY}\n"
    lines[start + 2 : end] = [
        f"| {day.isoformat()} | {material} | {summary} |\n"
        for day, material, summary in entries
    ]
    return "".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="JST date from distributed main")
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    args = parser.parse_args()
    original = args.readme.read_text(encoding="utf-8")
    updated = update_readme(original, args.date)
    if updated != original:
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=args.readme.parent, delete=False
            ) as stream:
                temporary = Path(stream.name)
                stream.write(updated)
            os.chmod(temporary, args.readme.stat().st_mode)
            os.replace(temporary, args.readme)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
