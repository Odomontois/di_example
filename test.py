import unittest

import mock.dialog
import sys
sys.modules["dialog"] = mock.dialog

from user import User


class UserSuite(unittest.TestCase):
    def test_dialog(self):
        user = User.by_dialog()
        self.assertEqual(user.name, "Ekaterina")
        self.assertEqual(user.age, 27)
        self.assertEqual(user.sex, "female")
        self.assertEqual(user.prefix, "Mrs")

if __name__ == "__main__":
    unittest.main()
