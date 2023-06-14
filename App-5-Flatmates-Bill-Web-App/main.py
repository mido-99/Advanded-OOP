from flask import Flask, render_template
from flask.views import MethodView
from wtforms import Form

app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")

class BillPage(MethodView):
    def get(self):
        return "Bill Page "

class ResultPage(MethodView):
    pass

class BillForm(Form):
    pass

app.add_url_rule('/', view_func=HomePage.as_view("home_page"))
app.add_url_rule('/bill', view_func=BillPage.as_view("bill_page"))


app.run(debug=True)

"""
Basically; Flask is based on functions (using the @app.route('/<route>')). Though we can work by OOP in which each class represents a webpage in our app.
So to tell Flask to treat this class as a func we write app.add_url_rule()

"""