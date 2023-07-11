import justpy as jp


# @jp.SetRoute('/')
def home():
    wp = jp.WebPage()
    dad = jp.Div(a= wp, classes='bg-gray-200 h-screen text-2xl p-8')
    
    jp.Div(a=dad, text="Hello from first Jp app!", classes='text-green-600')
    jp.Input(a=dad, placeholder='IIINNN', classes='form-input border border-blue-400 m-10 '
            'rounded')
    jp.Button(a=dad, text="press ME !", classes='hover:bg-white hover:text-red-400 rounded '
            'border border-blue-400')
    return wp



jp.Route("/", home)
jp.justpy()

"""
JustPy is an OOP framework to use just Python for building web apps without front-end
# steps:
1- Create a webpage instance wp
2- Add objects to the wp using a=wp attribute
3- Add the code into a function that's gonna be used as a request handler. 
#! REMEMBER this function should return the wp instance 
-------
To connect functions to their routes; We have 2 options:
1) Using jp.Route0(<route>, <function>)
2) Using @jp.SetRoute("<route>") decorator just before function declaration

"""