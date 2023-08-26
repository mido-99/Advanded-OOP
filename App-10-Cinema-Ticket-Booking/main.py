from classes.card import Card
from classes.seat import Seat
from classes.user import User
from classes.ticket import Ticket


def retry():    # Function to retry or quit in the while loop rather than writing it many times
    # sourcery skip: boolean-if-exp-identity, remove-unnecessary-cast
    next_step = input("Press 'R' to retry or 'Q' to quit: ")   
    return False if next_step in ['q', 'Q'] else True


# Main App CLI #
print("Welcome to our Cinema Seat Booking Service!\n"
    "Please Enter your data here:")
name = input("What's your name please? ")

loop = True      # Used to get input from user to choose next step; mostly to quit loop
while loop:
    
    seat_id = input("Which seat would you like to set on? [A1, A2, A3, B1, B2, B3]: ")
    seat = Seat(seat_id)

    if seat.valid() and seat.is_free(): # Obtain more info if seat is valid and free

        while retry:
            card_number = input("Ok, What's your card number please? ")
            cvc_number = input("Please enter your card CVC number: ")
            card_owner = input("And the Card holder: ")
            card = Card(card_number)
            
            if card.valid() and cvc_number == card.cvc and card_owner == card.owner:    # Get all card info
                
                if card.buy(seat):      # If enough money in the card
                    print("Purchase Successfully")
                else:
                    print("Not enough money to complete the purchase!")
                    if retry():
                        continue
                    
            else:       # If entered Data don't match those in database
                print("Sorry, No card in our data with these information!")
                if retry():
                    continue
            loop = False    # will be executed wherever user enters q in senarios above
            break    # Break the inner loop
            
    else:   # Seat is either invalid or booked
        if not seat.valid():         # assert that seat is valid
            print("Sorry, This seat doesn't exist!")
        elif not seat.is_free():        # assert that seat is free
            print("Unfortunately, this seat has been taken already :(")
            
        if retry():
            continue
        loop = False

ticket = Ticket(name, seat, card)
ticket.generate()
