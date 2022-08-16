def hello(name, age=6):
    """
    Print "Hello, {name}, {age}"
    """
    return f"Hello, {name}, {age}"


print(hello('Bob', 12))
print(hello.__doc__)
