import langdetect


text_1 = '米加州知事、ハリス上院議員の後任にパディラ州務長官を指名'
text_2 = '지속되는 물가상승률에 따라'
text_3 = 'Якби ви вчились так, як треба, То й мудрість би була своя.'
text_4 = 'Ein, zwei, drei, vier'
text_5 = 'Jesteś inwestorem, przedsiębiorcą lub osobą prywatną i szukasz atrakcyjnej nieruchomości?'


print(langdetect.detect_langs(text_1))
print(langdetect.detect_langs(text_2))
print(langdetect.detect_langs(text_3))
print(langdetect.detect_langs(text_4))
print(langdetect.detect_langs(text_5))
