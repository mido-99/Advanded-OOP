import random
import string
from fpdf import FPDF
from seat import Seat
from card import Card

class Ticket:
    """A Digital Ticket for user who bought a seat in our cinema"""

    def __init__(self, name, seat, card):
        self.name = name
        self.seat = seat
        self.card = card

        self.id = ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(6)
            )
        
    def generate(self):
        pdf = FPDF( orientation='p', unit='pt')
        pdf.add_page()

        # Label
        pdf.set_font('Helvetica', 'BU', 26)
        pdf.cell(w=0, h=40, txt="Cinema Ticket", align='C')
        pdf.ln(10*7)

        # Contents
        self._add_itme(pdf, "ID:")
        self._add_value(pdf, self.id)
        
        self._add_itme(pdf, "Name:")
        self._add_value(pdf, self.name)
        
        self._add_itme(pdf, "Seat:")
        self._add_value(pdf, self.seat.seat_id)
        
        self._add_itme(pdf, "Price:")
        self._add_value(pdf, f"{self.seat.price}$")
        
        pdf.output(f"tickets\{self.id}.pdf")
        
        
    def _add_itme(self, pdf, item):     # just not to rewrite font styles
        pdf.set_font('Times', 'IBU', 18)
        pdf.cell(150, 40, item)
        pdf.set_font('Times', size=18)
    
    def _add_value(self, pdf, value):
        pdf.cell(120, 40, value, ln=1)
        

card = Card(12345678)
seat = Seat("A3")

ticket = Ticket("name", seat, card)
ticket.generate()
