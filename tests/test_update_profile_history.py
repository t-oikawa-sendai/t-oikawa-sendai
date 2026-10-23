import unittest
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from scripts.update_profile_history import SUMMARY, update_readme


README = Path(__file__).resolve().parents[1] / "README.md"


class ProfileHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = README.read_text(encoding="utf-8")

    def test_new_date_updates_only_ai_field_and_five_history_rows(self):
        updated = update_readme(self.original, "2026-10-23")
        self.assertIn(f"2026-10-23。{SUMMARY}", updated)
        self.assertIn(f"| 2026-10-23 | AI活用入門 | {SUMMARY} |", updated)
        self.assertIn("| 2026-10-22 | AI活用入門 | 受講生向け配布ガイド", updated)
        self.assertNotIn("| 2026-10-05 | DokoTsubu", updated)
        self.assertEqual(5, len([line for line in updated.splitlines() if line.startswith("| 2026-")]))
        self.assertEqual(self.original.split("## 最近の更新")[0].split("- **教材の更新日・変更概要：** ")[0], updated.split("## 最近の更新")[0].split("- **教材の更新日・変更概要：** ")[0])

    def test_same_day_preserves_existing_specific_summary(self):
        self.assertEqual(self.original, update_readme(self.original, "2026-10-22"))

    def test_older_event_is_noop(self):
        self.assertEqual(self.original, update_readme(self.original, "2026-10-21"))

    def test_repeated_new_date_is_noop(self):
        updated = update_readme(self.original, "2026-10-23")
        self.assertEqual(updated, update_readme(updated, "2026-10-23"))

    def test_invalid_date_or_table_fails_before_mutation(self):
        with self.assertRaises(ValueError):
            update_readme(self.original, "2026-10-23|private")
        malformed = self.original.replace("|---|---|---|", "|---|---|")
        with self.assertRaises(ValueError):
            update_readme(malformed, "2026-10-23")
        self.assertEqual(self.original, README.read_text(encoding="utf-8"))

    def test_future_jst_date_is_rejected_without_changing_readme(self):
        tomorrow = (datetime.now(ZoneInfo("Asia/Tokyo")).date() + timedelta(days=1)).isoformat()
        with self.assertRaisesRegex(ValueError, "future"):
            update_readme(self.original, tomorrow)
        self.assertEqual(self.original, README.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
