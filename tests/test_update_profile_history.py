import unittest
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from scripts.update_profile_history import SUMMARY, update_readme


# Fixed inputs keep ordinary README updates from invalidating the regression tests.
ROWS = [
    "| 2026-10-22 | AI活用入門 | 受講生向け配布ガイドを追加しました。 |\n",
    "| 2026-10-21 | 教材A | 更新A。 |\n",
    "| 2026-10-20 | 教材B | 更新B。 |\n",
    "| 2026-10-19 | 教材C | 更新C。 |\n",
    "| 2026-10-18 | 教材D | 更新D。 |\n",
]
RECENT_ROWS = [
    "| 2026-10-24 | 教材A | 更新A。 |\n",
    "| 2026-10-24 | 教材B | 更新B。 |\n",
    "| 2026-10-24 | 教材C | 更新C。 |\n",
    "| 2026-10-23 | 教材D | 更新D。 |\n",
    "| 2026-10-23 | 教材E | 更新E。 |\n",
]
FIXTURE = """教材案内

### [AI活用入門（ai-setup-materials-student）](https://example.com/ai)

- **教材の更新日・変更概要：** 2026-10-22。受講生向け配布ガイドを追加しました。

---

### 別教材

- **教材の更新日・変更概要：** 2026-10-24。保持する説明。

## 最近の更新（直近5件）

| 更新日 | 教材 | 変更概要 |
|---|---|---|
""" + "".join(ROWS) + "\n末尾の説明も保持する。\n"
ROLLED_OFF = FIXTURE.replace("".join(ROWS), "".join(RECENT_ROWS))


class ProfileHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = FIXTURE

    def test_new_date_updates_only_ai_field_and_five_history_rows(self):
        updated = update_readme(self.original, "2026-10-23")
        expected = self.original.replace(
            "2026-10-22。受講生向け配布ガイドを追加しました。",
            f"2026-10-23。{SUMMARY}",
        ).replace(
            "".join(ROWS),
            f"| 2026-10-23 | AI活用入門 | {SUMMARY} |\n" + "".join(ROWS[:4]),
        )
        self.assertEqual(expected, updated)

    def test_same_day_preserves_existing_specific_summary(self):
        self.assertEqual(self.original, update_readme(self.original, "2026-10-22"))

    def test_older_event_is_noop(self):
        self.assertEqual(self.original, update_readme(self.original, "2026-10-21"))

    def test_repeated_new_date_is_noop(self):
        updated = update_readme(self.original, "2026-10-23")
        self.assertEqual(updated, update_readme(updated, "2026-10-23"))

    def test_new_event_after_ai_history_rolls_off(self):
        updated = update_readme(ROLLED_OFF, "2026-10-27")
        expected = ROLLED_OFF.replace(
            "2026-10-22。受講生向け配布ガイドを追加しました。",
            f"2026-10-27。{SUMMARY}",
        ).replace(
            "".join(RECENT_ROWS),
            f"| 2026-10-27 | AI活用入門 | {SUMMARY} |\n" + "".join(RECENT_ROWS[:4]),
        )
        self.assertEqual(expected, updated)
        self.assertEqual(updated, update_readme(updated, "2026-10-27"))

    def test_same_or_older_event_after_ai_history_rolls_off_is_noop(self):
        for event_date in ("2026-10-22", "2026-10-21"):
            with self.subTest(event_date=event_date):
                self.assertEqual(ROLLED_OFF, update_readme(ROLLED_OFF, event_date))

    def test_missing_ai_history_at_oldest_visible_date_is_allowed(self):
        tied = ROLLED_OFF.replace("2026-10-22。", "2026-10-23。")
        self.assertIn(f"2026-10-27。{SUMMARY}", update_readme(tied, "2026-10-27"))

    def test_missing_ai_history_inside_visible_date_range_is_rejected(self):
        inconsistent = ROLLED_OFF.replace("2026-10-22。", "2026-10-24。")
        with self.assertRaisesRegex(ValueError, "do not agree"):
            update_readme(inconsistent, "2026-10-27")

    def test_newer_ai_history_is_rejected_even_when_matching_row_exists(self):
        rows = ["| 2026-10-24 | AI活用入門 | 不整合な履歴。 |\n"] + ROWS[:4]
        inconsistent = FIXTURE.replace("".join(ROWS), "".join(rows))
        with self.assertRaisesRegex(ValueError, "do not agree"):
            update_readme(inconsistent, "2026-10-27")

    def test_only_older_ai_history_is_rejected(self):
        inconsistent = FIXTURE.replace("| 2026-10-22 | AI活用入門", "| 2026-10-21 | AI活用入門")
        with self.assertRaisesRegex(ValueError, "do not agree"):
            update_readme(inconsistent, "2026-10-27")

    def test_delayed_new_event_outside_visible_history_updates_only_detail(self):
        recent = ROLLED_OFF.replace("| 2026-10-23 |", "| 2026-10-24 |")
        expected = recent.replace(
            "2026-10-22。受講生向け配布ガイドを追加しました。",
            f"2026-10-23。{SUMMARY}",
        )
        self.assertEqual(expected, update_readme(recent, "2026-10-23"))
        self.assertEqual(expected, update_readme(expected, "2026-10-23"))

    def test_malformed_history_is_rejected(self):
        for rows in (ROWS[:4], ROWS[::-1], ["| broken row |\n"] + ROWS[1:]):
            with self.subTest(rows=rows):
                malformed = FIXTURE.replace("".join(ROWS), "".join(rows))
                with self.assertRaises(ValueError):
                    update_readme(malformed, "2026-10-27")

    def test_invalid_date_or_table_is_rejected(self):
        with self.assertRaises(ValueError):
            update_readme(self.original, "2026-10-23|private")
        malformed = self.original.replace("|---|---|---|", "|---|---|")
        with self.assertRaises(ValueError):
            update_readme(malformed, "2026-10-23")

    def test_future_jst_date_is_rejected(self):
        tomorrow = (datetime.now(ZoneInfo("Asia/Tokyo")).date() + timedelta(days=1)).isoformat()
        with self.assertRaisesRegex(ValueError, "future"):
            update_readme(self.original, tomorrow)


if __name__ == "__main__":
    unittest.main()
