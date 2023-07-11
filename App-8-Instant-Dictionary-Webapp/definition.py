import pandas


class definition:
    
    def __init__(self, term):
        self.term = term
        
    def get(self):
        df = pandas.read_csv('data.csv')
        return tuple(df[df['word'] == self.term]['definition'])

print(definition('sun').get())