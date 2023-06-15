from fpdf import FPDF

class Bill():
    '''Data about period and bill amount'''
    
    def __init__(self, period, amount):
        self.period = period
        self.amount = int(amount)
        
class Flatmate():
    '''Typically representing a person who shares a room and the bill'''
    
    def __init__(self, name, time_at_home):
        self.name = name
        self.time_at_home = time_at_home
        
    # calculate each flatmate's pay
    def pays(self, bill, flatmate_2):
        ratio = int(self.time_at_home) / (int(self.time_at_home) + int(flatmate_2.time_at_home))
        pay = round(ratio * bill.amount, 2)
        return pay

class PdfReport():
    '''a Pdf file after payment calculation'''
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        # Creating pdf file and adding an icon
        pdf = FPDF( orientation='p', unit='pt')
        pdf.add_page()
        pdf.image(name=r'files\house.png', w=40, h=40)
        
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
        pdf.cell(120, 40, str(bill.amount)+' $')
        pdf.ln(100)
        pdf.set_font('Times', '', 24)
        pdf.cell(260, 40, flatmate1.name, align='C')
        pdf.cell(260, 40, flatmate2.name, align='C', ln=1)
        pdf.cell(260, 40, flatmate1_pay, align='C')
        pdf.cell(260, 40, flatmate2_pay, align='C', ln=1)
        
        pdf.output(self.filename) if self.filename.endswith('.pdf') else pdf.output(self.filename+'.pdf')
        # webbrowser.open(self.filename)
