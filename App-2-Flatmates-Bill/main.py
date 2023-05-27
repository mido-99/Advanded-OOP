import webbrowser
from fpdf import FPDF
from my_funcs import confirm_no_empty_str, confirm_input_is_number
from utility import Bill, Flatmate, PdfReport

## CLI app ##

# getting inputs from the user
user1_name = confirm_no_empty_str("Hey! This app will help you to calculate how much you should pay for your flat bill.\nCould you enter your name please: ")
user2_name = confirm_no_empty_str("Your flatmate's name too please: ")
bill_period = confirm_no_empty_str("And for which month? (ex:- May 2023): ")

bill_amount = confirm_input_is_number("So, How much is your bill? ")
user_period = confirm_input_is_number("OK, How many days have you been in the house in that period? ")
flatmate_period = confirm_input_is_number("And how many days for your flatmate? ")

# creating instances out of data provided
user1 = Flatmate(user1_name, user_period)
user2 = Flatmate(user2_name, flatmate_period)
bill = Bill(bill_period, bill_amount)
user_pay = user1.pays(bill=bill, flatmate_2=user2)
print(f"\nWell well... Here's your pay for this month!... {user_pay} And your flatmate should pay {bill.amount-user_pay}\n")

# If user wants a pdf report
while True:
    want_report = input("So do you want a pdf report for this month? (y/n): ")

    if want_report in ["y", "Y", "Yes", "yes", "YES"]:
        print("Sure! We have created it for you.")
        pdf= PdfReport(filename=f'{bill.period} bill.pdf')
        pdf.generate(user1, user2, bill=bill)
        
    elif want_report in ["N", 'n', "NO", 'no', "No"]:
        print("Ok. Thank you for using this simple app & have a good day!")
    
    else:
        print("Please enter a valid value!")
        continue
    break

