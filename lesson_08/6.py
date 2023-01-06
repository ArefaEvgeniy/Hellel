def shout(word="Yes"):
    return word + "!"


print(shout())

scream = shout

print(scream())

del shout
print('-' * 50)

print(scream())
