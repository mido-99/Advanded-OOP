import sqlite3

class Seat:
    """A Seat in cinema! with its data of course: id, booked, price, and so"""
    database = 'cinema.db'
    
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self._validate_card()
    
    def _get_info(self):   # sourcery skip: assign-if-exp, remove-unreachable-code, use-named-expression
        '''Check whether this seat is free or booked'''
        
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT * FROM seat WHERE seat_id=?''', (self.seat_id,)
        )
        result = cursor.fetchall()
        connection.close()
        return result
        
    def _validate_card(self):  # sourcery skip: use-named-expression
        '''Vallidate if the card exists'''
        
        result = self._get_info()
        if result:
            self.seat_id, self.taken, self.price = result[0]
            # return result[0][0]
            return self.seat_id, self.taken, self.price
        else:
            return False #"Sorry, This seat doesn't exist!"
        
    def is_free(self):
        """Returns True if seat is free, just opposite to taken"""
        return not self.taken
    
    def book(self, card):  # sourcery skip: use-named-expression
        bought = card.buy(self)
        
        if bought:
            connection = sqlite3.connect(self.database)
            connection.execute(
            '''UPDATE seat SET taken=? WHERE seat_id=?''', 
            (1, self.seat_id)
            )
            connection.commit()
            connection.close()
            return True
        else:
            return False
            

# seat1 = Seat("A1")
# print(seat1._validate_card())
# print(seat1.taken)
# print(seat1.is_free())