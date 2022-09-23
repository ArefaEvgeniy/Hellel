
def summa(a, b):
    try:
        return a + b
    except TypeError:
        print('Not support type')
    except Exception:
        print('Something is wrong')


def mines(a, b):
    return a - b
