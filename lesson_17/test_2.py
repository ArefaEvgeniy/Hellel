import unittest

from work_1 import mines


class TestMines(unittest.TestCase):

    def test_wrong(self):
        with self.assertRaises(TypeError):
            mines(4, '5')


if __name__ == '__main__':
    unittest.main()
