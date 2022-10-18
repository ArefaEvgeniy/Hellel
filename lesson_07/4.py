def hello(age: int, name: str = 'world') -> str:
    """
    Test Docs
    """
    return 'Hello, ' + str(name)


print(hello(23))
print(hello.__annotations__)
print(hello.__doc__)
print(print.__doc__)
