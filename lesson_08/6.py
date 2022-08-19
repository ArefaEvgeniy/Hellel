def get_talk(type="shout"):
    def shout(word='да'):
        return word.upper() + '!'

    def whisper(word='да'):
        return word.lower() + '...'

    if type == "shout":
        return shout
    else:
        return whisper


talk = get_talk()

print(talk())

print(get_talk('whisper')())
