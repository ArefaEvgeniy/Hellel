def func(a: int, b: int = 0) -> str:
    """
    This is my test function
    :param a: number of months
    :param b: state
    :return: result of dept
    """
    c = a + b
    return str(c)


z = func('rte', 'fhdj')
print(z)
print(type(z))
print(func.__annotations__)
print(func.__doc__)
