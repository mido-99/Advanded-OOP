import pandas


class Definition:
    
    def __init__(self, term):
        self.term = term
        
    def get(self):
        '''Get a Definition for a word or a phrase'''
        df = pandas.read_csv('data.csv')
        return tuple(df[df['word'] == self.term]['definition'])

if __name__ == '__main__':
    print(Definition('sun').get())