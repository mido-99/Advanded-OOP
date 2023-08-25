import random
import string
import fpdf


class Ticket:
    """A Digital Ticket for user who bought a seat in our cinema"""

    def __init__(self, name, sead_id, price):
        self.name = name
        self.sead_id = sead_id
        self.price = price
        self.id = ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(6)
            )
        
    def generate(self):
        pass

