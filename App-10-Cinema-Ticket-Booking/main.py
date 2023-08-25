from classes.card import Card
from classes.seat import Seat
from classes.ticket import Ticket

print("Welcome to our Cinema Seat Booking Service!\n"
    "Please Enter your data here:")
user = input("What's your name please? ")

while True:
    seat_id = input("Which seat would you like to set on? [A1, A2, A3, B1, B2, B3]: ")
    seat = Seat(seat_id)
        
    if not seat.valid() or not seat.is_free():
        
        if not seat.valid():         # assert that seat is valid
            print("Sorry, This seat doesn't exist!")
        elif not seat.is_free():        # assert that seat is free
            print("Unfortunately, this seat has been taken already :(")
        
        inp_1 = input("Press 'R' to try another place or 'Q' to quit: ")     # Next action
        if inp_1 in ['r', 'R']:
            continue
        elif inp_1 in ['q', 'Q']:
            break
    
    else:
        pass # rest of code after seat is validated
