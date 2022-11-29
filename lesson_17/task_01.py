def summa(a, b):
    try:
        return a + b
    except TypeError:
        print('Not support type')
    except Exception:
        print('Something is wrong')
    return None


def mines(a, b):
    return a - b


# if __name__ == "__main__":
#     import doctest
#     doctest.testfile('test.txt')
