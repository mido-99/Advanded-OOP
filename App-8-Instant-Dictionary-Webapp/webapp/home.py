import justpy as jp
import requests
import definition
from webapp import layout
from webapp import page


class Home(page.Page):
    path = '/'
    
    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        
        # initialize webpage
        wp = jp.QuasarPage(tailwind=True)
        
        # Adding a default layout on which page content will be displayed
        lay = layout.LayoutDefault(a=wp)
        container = jp.QPageContainer(a=lay)
        dad = jp.Div(a= container, classes='bg-gray-200 h-screen text-xl p-8')
        
        # Page description
        jp.Div(a= dad, text='Instant Dictionary', classes='text-4xl font-italic')
        jp.Div(a= dad, text='Type any word or phrase ', classes='')
        
        inp_div = jp.Div(a= dad, classes='grid grid-cols-2 gap-4 m-8') #*2
        
        # View definition
        definition = jp.Div(a=dad, text='Definition here', classes='border-8 border-green-300 h-80'
                        ' border-double')
        # User input
        term = jp.Input(a=inp_div, classes='border-4 rounded-md'
                        ' bg-gray-100 focus:bg-white focus:border-green-400 focus:outline-none'
                        ' border-green-300', definition=definition)
        term.on('input', cls.get_def)
        
        return wp

# Works:
    @staticmethod
    def get_def(widget, msg):
        final_def = definition.Definition(widget.value).get()
        
        if isinstance(final_def, tuple):
            final_str = '\n'.join(f'{i+1}) {string}' for i, string in enumerate(final_def))
        else:
            final_str = final_def    
        widget.definition.text = final_str


#! Non-working code:
"""
    @staticmethod
    def get_def(widget, msg):
        
        print("get_def started")  # Debug message
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        print("Request sent")  # Debug message
        data = req.json()
        print("Response received")  # Debug message
        
        # final_def = definition.Definition(widget.value).get()
        widget.definition.text = ''.join(data['word'])        
"""
#! An issue is occuring during sending request to the api, don't know why but it stucks
#! Otherwise everything should work and we can use the api to get word's  definitions, 
#! rather than using Definition class directly.

"""
#* REMEMBER that if we use self like this:
    def get_def(self):
As mentioned in main file; We're not working with class instances, with the class itself instead.
So if we consider using @classmethod; We are pushed then to use cls like this:
    @classmethod
    def get_def(cls):
Thus we can't use widget, msg which is our main goal.

* The solution in such case is To use @staticmethod simply. Since they don't require args like
self and cls, so they could be used inside a class to do a specific function without either 
refering to class like @classmethod, or instantiating an instance of it like @classmethod

#*2 This div is actually not necessary, just made to contain input. As I needed to use definitions
inside term and not get referenced before assignment error

"""