import sqlite3
# from seat import Seat
[1, 1253, 3416 , 132]

class Card:
    """Card object with info about user's card like: number, cvc number, balance, etc.."""
    database = 'banking.db'

    def __init__(self, number):
        self.number = number
        self.valid()
    
    def _get_info(self):  # sourcery skip: use-named-expression
        '''Get information about Card from database'''
        
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT * FROM card WHERE number=? ''', (self.number,)
        )
        result = cursor.fetchall()
        connection.close()
        return result
    
    def valid(self):  # sourcery skip: use-named-expression
        '''Vallidate the card: if the card exists returns its properties,
        else returns False
        '''
        
        result = self._get_info()
        if result:
            self.type, self.number, self.cvc, self.owner, self.balance = result[0]      #fetchall() returns a list even if one row, so select first and only tuple
            return self.type, self.cvc, self.owner, self.balance
        else:
            return False #'No card with this number!'
    
    def buy(self, seat):
        '''Buy a seat; substract the price and book it in cinema database'''
        price = seat.price
        
        if self.balance >= price:
            connection = sqlite3.connect(self.database)
            connection.execute(
            '''UPDATE card SET balance=? WHERE number=?''', 
            (self.balance - price, self.number)
            )
            connection.commit()
            connection.close()
            
            seat.book()
            return True #"Success!"
        else:
            return False #"Not enough balance to purchase!"

# card = Card(12345678)
# print(card.valid())

# seat1 = Seat("A2")

# print(card.buy(seat1))
