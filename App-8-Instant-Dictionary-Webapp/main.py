import justpy as jp


# @jp.SetRoute('/')
def home():
    wp = jp.WebPage()
    # main div for the whole page. Used for fullscreen bg color and padding
    dad = jp.Div(a= wp, classes='bg-gray-200 h-screen text-xl p-8')
    
    div1 = jp.Div(a=dad, classes='grid grid-cols-2 my-4 gap-6')
    jp.Input(a=div1, placeholder='Type in', classes='border-4 border-blue-400'
            ' rounded-l')
    jp.Input(a=div1, placeholder='An input', classes='form-input border-4 border-blue-400')
    jp.Div(a=div1, text="Hello from first Jp app!", classes='text-green-600')
    jp.Div(a=div1, text="Trial elements", classes='text-green-600')
    
    div2 = jp.Div(a=dad, classes='grid grid-cols-2 gap-6 justify-items-center')
    jp.Button(a=div2 , text="press ME !", classes='hover:bg-white hover:text-red-400 rounded'
            ' border border-blue-400 w-1/2 ')
    jp.Div(a=div2, text="Second div", classes='text-red-600')
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