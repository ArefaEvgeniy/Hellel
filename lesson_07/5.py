def get_input_data():
    return int(input("enter integer number "))

def make_tasks_with_wile(input_data):

    null = 0
    summa = 0

    while null <= input_data:
        null = null+1
        if not null %3 == 0:
            summa = summa+null*null*null
    print(summa)


def make_tasks_with_for(input_data):

    null = 0
    summa = 0

    for null in range(0, input_data):
        summa = summa+null*null*null
        print(summa)


out_number = get_input_data()
make_tasks_with_wile(out_number)

make_tasks_with_for(out_number)
