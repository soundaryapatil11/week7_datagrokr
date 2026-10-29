import unittest

from app import create_task, complete_task


class TaskTrackerTests(unittest.TestCase):
    def test_create_task_strips_title_and_normalizes_priority(self):
        task = create_task("  Water plants  ", "HIGH")
        self.assertEqual(task["title"], "Water plants")
        self.assertEqual(task["priority"], "high")
        self.assertFalse(task["completed"])

    def test_create_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            create_task("   ")

    def test_create_task_rejects_unknown_priority(self):
        with self.assertRaises(ValueError):
            create_task("Water plants", "urgent")

    def test_complete_task_returns_completed_copy(self):
        original = create_task("Check pump")
        completed = complete_task(original)
        self.assertTrue(completed["completed"])
        self.assertFalse(original["completed"])


if __name__ == "__main__":
    unittest.main()
