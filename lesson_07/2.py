def hello(name: str, age: int = 6) -> str:
    return f"Hello, {name}, {age}"


print(hello.__annotations__)

print(hello('Bob', 12))
print(hello('Jack'))
