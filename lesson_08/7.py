def talk(type="shout"):
    def shout(word="Yes"):
        return word + "!"

    def whishper(word="Yes"):
        return word.lower() + '...'

    if type == "shout":
        return shout
    else:
        return whishper



print(talk()("ts"))
