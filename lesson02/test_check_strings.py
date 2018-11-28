import unittest
from check_strings import check_strings


class TestStrings(unittest.TestCase):
    def test_strings_type(self):
        self.assertEqual(check_strings(1, 1), 0)
        self.assertEqual(check_strings('1', 1), 0)
        self.assertEqual(check_strings(1, '1'), 0)
        self.assertEqual(check_strings('1', '1'), 1)

    def test_strings_equality(self):
        self.assertEqual(check_strings('ball', 'ball'), 1)

    def test_second_word_is_lears(self):
        self.assertEqual(check_strings('ball', 'learn'), 3)

    def test_other_cases(self):
        self.assertEqual(check_strings('ball', 'baseball'), None)


if __name__ == '__main__':
    unittest.main()

