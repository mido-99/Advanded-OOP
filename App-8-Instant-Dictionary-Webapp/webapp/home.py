import justpy as jp

class Home():
    path = '/'
    
    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        dad = jp.Div(a= wp, classes='bg-gray-200 h-screen text-xl p-8')
        
        jp.Div(a= dad, text='Instant Dictionary', classes='text-4xl font-italic')
        jp.Div(a= dad, text='Type any word or phrase ', classes='')
        
        inp_div = jp.Div(a= dad, classes='grid grid-cols-2 gap-4 m-8')
        term = jp.Input(a=inp_div, placeholder='Type here...', classes='border-4 rounded-md'
                        ' bg-gray-100 focus:bg-white focus:border-purple-600 focus:outline-none'
                        ' border-purple-400')
        definition = jp.Div(a=dad, text='Definition here', classes='border-8 border-purple-400 h-40'
                        ' border-double')
        btn = jp.Button(a=inp_div, text="what does this mean?", classes='border-4 border-purple-400'
                        ' rounded-md outline-none', 
                        click=cls.get_def, term=term, definition=definition)
        return wp
    
    @staticmethod
    def get_def(widget, msg):
        widget.definition.text = 'Boom'


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
"""