def shout(word="Да"):
    return word + "!"


print(shout())

scream = shout

print(scream('22'))

del shout
# print(shout())
print(scream())


def do_some_before(func):
    print("Before")
    print(func())
    print("After")


do_some_before(scream)
