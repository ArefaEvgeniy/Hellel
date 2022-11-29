import unittest
from task_01 import mines


class TestMines(unittest.TestCase):

    def test_int_float(self):
        self.assertEqual(mines(10, 0), 10)
        self.assertEqual(mines(4, 5.0), -1.0)


class TestWrongData(unittest.TestCase):

    def test_wrong(self):
        with self.assertRaises(TypeError):
            mines(10, '5')


# if __name__ == "__main__":
#     unittest.main()
