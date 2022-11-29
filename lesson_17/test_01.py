import unittest
from task_01 import summa


class TestSumma(unittest.TestCase):

    # @unittest.skip('Not implemented yet')
    def test_int_float(self):
        self.assertEqual(summa(4, 5), 9)
        self.assertEqual(summa(4, 5.0), 9.0)

    def test_str(self):
        self.assertEqual(summa('4', '5'), '45')


class TestWrongData(unittest.TestCase):

    def test_wrong(self):
        self.assertEqual(summa(4, None), None)
        self.assertEqual(summa(4, '5'), None)


# if __name__ == "__main__":
#     unittest.main()
