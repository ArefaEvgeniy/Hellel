class FoundException(Exception): pass

table = [
    ['2344', 'dfgtr', 'ddfggg'],
    ['qwertt', 'p][poii'],
    ['asddff', '0987654321'],
    ['zxcvb', 'mnbvcvlkjjh', 'ffff']
]

target = 'R'

row = column = index = None
found = False
for row, record in enumerate(table):
	for column, field in enumerate(record):
		for index, item in enumerate(field):
			if item == target:
				found = True
				break
		if found:
			break
	if found:
		break
if found:
	print("found at ({0}, {1}, {2})".format(row+1, column+1, index+1))
else:
	print("not found")


row = column = index = None
try:
	for row, record in enumerate(table):
		for column, field in enumerate(record):
			for index, item in enumerate(field):
				if item == target:
					raise FoundException
except FoundException:
	print("found at ({0}, {1}, {2})".format(row+1, column+1, index+1))
else:
	print("not found")
