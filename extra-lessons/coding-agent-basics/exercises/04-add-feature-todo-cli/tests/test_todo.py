import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "starter"))

from todo import add_task, complete_task, list_all_tasks, list_open_tasks


class TodoTests(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        add_task(tasks, "learn codex")
        self.assertEqual(tasks, [{"title": "learn codex", "done": False}])

    def test_complete_task(self):
        tasks = [{"title": "learn codex", "done": False}]
        complete_task(tasks, "learn codex")
        self.assertTrue(tasks[0]["done"])

    def test_list_all_tasks(self):
        tasks = [
            {"title": "learn codex", "done": False},
            {"title": "join zoom", "done": True},
        ]
        self.assertEqual(list_all_tasks(tasks), tasks)

    def test_list_open_tasks(self):
        tasks = [
            {"title": "learn codex", "done": False},
            {"title": "join zoom", "done": True},
            {"title": "review diff", "done": False},
        ]
        self.assertEqual(
            list_open_tasks(tasks),
            [
                {"title": "learn codex", "done": False},
                {"title": "review diff", "done": False},
            ],
        )


if __name__ == "__main__":
    unittest.main()
