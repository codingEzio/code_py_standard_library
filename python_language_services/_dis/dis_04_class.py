import dis


class Obj:
    ''' example for dis '''

    CLASS_ATTR = 'some val'

    def __str__(self):
        return 'Obj({})'.format(self.name)  # won't get same res if using f''

    def __init__(self, name):
        self.name = name


dis.dis(Obj)
