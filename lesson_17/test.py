import unittest

from work_1 import summa


class TestSumma(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def setUpClass(cls) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def tearDownClass(cls) -> None:
        pass

    def test_summa(self):
        self.assertEqual(summa(4, 5), 9)
        self.assertEqual(summa(-2, 3.0), 1.0)
        self.assertNotEqual(summa(4, 5), 0)

    def test_wrong(self):
        self.assertEqual(summa(4, None), None)
        self.assertEqual(summa(4, '5'), None)


class TestSummaStr(unittest.TestCase):

    def test_str(self):
        self.assertEqual(summa('4', '5'), '45')
        self.assertEqual(summa('0', '0'), '00')


if __name__ == '__main__':
    unittest.main()
