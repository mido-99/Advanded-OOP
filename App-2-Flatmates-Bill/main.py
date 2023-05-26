import webbrowser
from fpdf import FPDF
    
class Bill():
    '''Data about period and bill amount'''
    
    def __init__(self, period, amount):
        self.period = period
        self.amount = amount
        
class Flatmate():
    '''Typically representing a person who shares a room and the bill'''
    
    def __init__(self, name, time_at_home):
        self.name = name
        self.time_at_home = time_at_home
        
    # calculate each flatmate's pay
    def pays(self, bill, flatmate_2):
        ratio = self.time_at_home / (self.time_at_home + flatmate_2.time_at_home)
        pay = ratio * bill.amount
        return round(pay, 2)
    
class PdfReport():
    '''a Pdf file after payment calculation'''

    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        # Creating pdf file and adding an icon
        pdf = FPDF( orientation='p', unit='pt')
        pdf.add_page()
        pdf.image(name='house.png', w=40, h=40)
        
        # Label
        pdf.set_font('Helvetica', 'BU', 26)
        pdf.cell(w=0, h=40, txt="Flatmates Bill", align='C', ln=1)
        
        # Contents
        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate2.pays(bill, flatmate1))
        pdf.set_font('Times', 'IB', 18)
        pdf.cell(150, 40, "Period:")
        pdf.cell(120, 40, bill.period, ln=1)
        pdf.cell(150, 40, "Bill Amount:")
        pdf.cell(120, 40, str(bill.amount)+'$')
        pdf.ln(100)
        pdf.set_font('Times', '', 24)
        pdf.cell(260, 40, flatmate1.name, align='C')
        pdf.cell(260, 40, flatmate2.name, align='C', ln=1)
        pdf.cell(260, 40, flatmate1_pay, align='C')
        pdf.cell(260, 40, flatmate2_pay, align='C', ln=1)
        
        pdf.output(self.filename) if self.filename.endswith('.pdf') else pdf.output(self.filename+'.pdf')
        # webbrowser.open(self.filename)

## CLI app ##
while True:
    user1 = input("Hey! This app will help you to calculate how much you should pay for your flat bill.\nCould you enter your name please: ")
    if user1 == "":
        print("Empty input!")
        continue
    break

while True:
    user2 = input("Your flatmate's name too please: ")
    if user2 == "":
        print("Empty input!")
        continue
    break

while True:
    bill_period = input("And for which month? (ex:- May 2023): ")
    if bill_period == "":
        print("Empty input!")
        continue
    break

while True:
    try:
        bill_amount = float(input("So, How much is your bill? "))
    except ValueError:
        print("Please enter a number!")
        continue
    break

while True:
    try:
        user_period = float(input("OK, How many days have you been in the house in that period? "))
    except ValueError:
        print("Please enter a number!")
        continue
    break

while True:
    try:
        flatmate_period = float(input("And how many days for your flatmate? "))
    except ValueError:
        print("Please enter a number!")
        continue
    break

user1 = Flatmate(user1, user_period)
user2 = Flatmate(user2, flatmate_period)
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
        print("It's Ok. Thank you for using this simple app & have a good day!")
    else:
        print("Please enter a valid value!")
        continue
    break

