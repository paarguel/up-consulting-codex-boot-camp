import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "starter"))

from hello import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_uses_name(self):
        self.assertEqual(greeting("Ada"), "Hello, Ada!")

    def test_greeting_works_for_friend(self):
        self.assertEqual(greeting("friend"), "Hello, friend!")


if __name__ == "__main__":
    unittest.main()
