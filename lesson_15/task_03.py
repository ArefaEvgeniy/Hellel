class FoundException(Exception):
    def __init__(self, message='My new exception'):
        super().__init__(message)


table = [['123', '4567', '890'], ['qwert', 'yuiop', 'asdf'], ['hjkl', 'zxcvb', 'nm']]
target = '0'


found = False
row, column, index = None, None, None
try:
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    raise FoundException()
except FoundException as err:
    print("found at ({0}, {1}, {2})".format(row+1, column+1, index+1), err)
else:
    print("not found")
