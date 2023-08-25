class User:
    """A standard user who buys a ticket for a seat in the cinema"""

    def __init__(self, name):
        self.name = name

    def make_purchase(self, seat, card):
        '''The top method for triggering purchase operation's other methods'''
        
        # if not seat.valid():
        #     return "Sorry, This seat doesn't exist!"
        elif not card.valid():
            return "Sorry, No card in our data with this number!"
        # elif not seat.is_free():
        #     return "Unfortunately, this seat has been taken already :("
        else:
            try:
                seat.book(card)
                return "Purchase Successfully!"
            except Exception as e:
                return e
#? Conditions are taken as they are into main. #Commented are already in main

# seat = Seat('A1')
# card = Card(12345678)

# user1 = User('momo')
# print(user1.make_purchase(seat, card))