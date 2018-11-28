import unittest
import add


class TestAdd(unittest.TestCase):
    def test_types(self):
        self.assertIsNone(add.add('ball', 1))
        self.assertIsNone(add.add(1, 'ball'))

    def test_add(self):
        self.assertEqual(add.add(6, 8), 14)


if __name__ == '__main__':
    unittest.main()