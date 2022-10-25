def talk(type='shout'):
    def shout(word='yes'):
        return word + '!'

    def whisper(word='yes'):
        return word + '...'

    if type == 'shout':
        return shout
    else:
        return whisper


test = talk('ffgt')
print(test())
