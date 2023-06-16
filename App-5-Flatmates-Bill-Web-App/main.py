from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flatmates_bill import utility

app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")

class BillPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form.html", bill_form=bill_form)
    
    def post(self):
        bill_form = BillForm(request.form)
        
        # Processing the user data
        bill = utility.Bill(bill_form.period.data, bill_form.amount.data)
        flatmate1 = utility.Flatmate(bill_form.name_1.data, bill_form.days_1.data)
        flatmate2 = utility.Flatmate(bill_form.name_2.data, bill_form.days_2.data)
        
        return render_template('bill_form.html',
                                bill_form=bill_form,
                                result = True,
                                name1 = flatmate1.name,
                                amount1 = flatmate1.pays(bill, flatmate2),
                                name2 = flatmate2.name,
                                amount2 = flatmate2.pays(bill, flatmate1))


# class ResultPage(MethodView): #*2
    
#     def post(self):
#         bill_form = BillForm(request.form)
        
#         # Processing the user data
#         bill = utility.Bill(bill_form.period.data, bill_form.amount.data)
#         flatmate1 = utility.Flatmate(bill_form.name_1.data, bill_form.days_1.data)
#         flatmate2 = utility.Flatmate(bill_form.name_2.data, bill_form.days_2.data)
        
#         return render_template('result.html',
#                                 name1 = flatmate1.name,
#                                 amount1 = flatmate1.pays(bill, flatmate2),
#                                 name2 = flatmate2.name,
#                                 amount2 = flatmate2.pays(bill, flatmate1))

class BillForm(Form): #*
    amount = StringField('Amount:')
    period = StringField('Period:')
    name_1 = StringField('Name:')
    days_1 = StringField('Days in the house:')
    name_2 = StringField('Name:')
    days_2 = StringField('Days in the house:')
    button = SubmitField("Calculate")

app.add_url_rule('/', view_func=HomePage.as_view("home_page"))
app.add_url_rule('/bill', view_func=BillPage.as_view("bill_form"))
# app.add_url_rule('/result', view_func=ResultPage.as_view("result_page"))


app.run(debug=True)

"""
Basically; Flask is based on functions (using the @app.route('/<route>')). Though we can work by OOP in which each class represents a webpage in our app.
So to tell Flask to treat this class as a func we write app.add_url_rule()

#* The basic way of building a form in Flask is by manually writing its code in the html page inside the <form> like <input> and <label> and so. But a better way to do that is by defining everything in python code. and here are the steps:

1. Make your own form class that inherits from wtform.Form; in which we use SubmitField, StringField (This field is the base for most of the more complicated fields, and represents an <input type="text">.)...

2. In the page class which will contain the form in its html; instantiate an instance of that form class.

3. Return that object in the render_template(var=object) by passing it to a variable -They're not the same though having the same name.

4. In the html form; inject the python code for that var and its properties: form_name.form_class_var.property

#*2 Getting data from the form
1. To achieve this; in the form tag add method="post" and action="/route".
2. in the python class for that route, def post() not get and create an object of the form but NOTE this time pass to it request.form
3. Now we have the form data! and the way we access any of its field is: form_name.form_class_var.data

#*3 To view the rusult in the same page:
1. Change the form action=<same_page> 
2. Comment the add_rule for that route (as it's no more needed)
3. Now when the button is pressed, a POST request is sent to the server so we need to define a post() for this page. Fortunately; it does the same as the deprecated page so we can just copy its code and paste it
#! Dont't forget to return the smae .html file and also define any variable that's not defined in the render_template(new.html, var=var) )
4. 
"""