import unittest

from person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person_1 = Person('Иван', 'Петров', 'Сидорович', '20.11.1980', '', 'm')
        self.person_1.valid()
        self.person_2 = Person('Tom', 'Black', '', '3.5.2010', '', 'm')
        self.person_2.valid()
        self.person_3 = Person('Natali', 'Kid', '', '15.9.1974', '14.9.1999', 'f')
        self.person_3.valid()

    def test_str(self):
        self.assertEqual(self.person_1.__str__(),
                         'Иван Петров Сидорович 41 год, мужчина. Родился: 20.11.1980.')
        self.person_1.sex = 'f'
        self.assertEqual(self.person_1.__str__(),
                         'Иван Петров Сидорович 41 год, женщина. Родилась: 20.11.1980.')
        self.assertEqual(self.person_2.__str__(),
                         'Tom Black 12 лет, мужчина. Родился: 03.05.2010.')
        self.assertEqual(self.person_3.__str__(),
                         'Natali Kid 24 года, женщина. Родилась: 15.09.1974. Умерла: 14.09.1999.')

    def test_full_name(self):
        self.assertEqual(self.person_1.full_name, 'Иван Петров Сидорович')
        self.assertEqual(self.person_2.full_name, 'Tom Black')
        self.assertEqual(self.person_3.full_name, 'Natali Kid')

    def test_print_age(self):
        self.assertEqual(self.person_1.print_age, '41 год')
        self.assertEqual(self.person_2.print_age, '12 лет')
        self.assertEqual(self.person_3.print_age, '24 года')

    def test_valid(self):
        self.assertTrue(self.person_1.valid())
        self.assertTrue(self.person_2.valid())
        self.assertTrue(self.person_3.valid())

        person_wrong_1 = Person('', '', '', '20.11.1980', '14.9.1999', 'm')
        self.assertFalse(person_wrong_1.valid())
        self.assertEqual(person_wrong_1.error, 'Вы не ввели имя')

        person_wrong_2 = Person('Иван', '', '', '', '14.9.1999', 'm')
        self.assertFalse(person_wrong_2.valid())
        self.assertEqual(person_wrong_2.error, 'Ошибка при вводе даты рождения')

        person_wrong_3 = Person('Natali', 'Kid', '', '15.9.1974', '14.9.1973', 'f')
        self.assertFalse(person_wrong_3.valid())
        self.assertEqual(person_wrong_3.error, 'Возраст не может быть отрицательным')

        person_wrong_4 = Person('Natali', 'Kid', '', '15.9.1974', '14.9.1975', 'ж')
        self.assertFalse(person_wrong_4.valid())
        self.assertEqual(person_wrong_4.error, 'Ошибка ввода пола')


if __name__ == '__main__':
    unittest.main()
