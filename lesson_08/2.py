# Приведен список баллов 10 студентов на экзамене по химии.
# Отфильтровать тех, кто сдал с баллом выше 75 ... используя filter().

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]


def is_A_student(x):
    return x > 75


over_75 = list(filter(is_A_student, scores))
over_75_2 = list(filter(lambda x: x > 75, scores))
print(over_75)
print(over_75_2)
