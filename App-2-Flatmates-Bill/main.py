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
        
    def pays(self, bill, flatmate_2):
        ratio = self.time_at_home / (self.time_at_home + flatmate_2.time_at_home)
        pay = ratio * bill.amount
        return pay
    
class PdfReport():
    '''a Pdf file after payment calculation'''
    def __init__(self, filename):
        pass
    
    def generate(self, flatmate1, flatmate2, bill):
        pass
    
tom = Flatmate('Tom', 20)
jerry = Flatmate('Jerry', 25)

bill_march = Bill('March 2023', 121)

print(tom.pays(bill_march, jerry))
