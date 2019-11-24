
import operator
import itertools


class Dictionary:
    ''' note: the `words` file was opened in the 'test_loop' file!! '''

    def __init__(self, words):
        self.by_letter = {}
        self.load_data(words)

    def load_data(self, words):
        ''' By using itertools, the iteration is moved to C.
            Well, faster!
        '''

        grouped = itertools.groupby(
            words, 
            key=operator.itemgetter(0),
        )

        self.by_letter = {
            group[0][0]: group for group in grouped
        }