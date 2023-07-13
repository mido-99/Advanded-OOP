import justpy as jp


# @jp.SetRoute('/')
def home():
    wp = jp.QuasarPage(tailwind=True) #*3
    # main div for the whole page. Used for fullscreen bg color and padding
    dad = jp.Div(a= wp, classes='bg-gray-200 h-screen text-xl p-8') #*
    
    div1 = jp.Div(a=dad, classes='grid grid-cols-2 my-4 gap-6')
    inp1 = jp.Input(a=div1, placeholder='Type in', classes='border-4 border-blue-400'
            ' rounded-l')
    inp2 = jp.Input(a=div1, placeholder='An input', classes='form-input border-4 border-blue-400')
    jp.Div(a=div1, text="Hello from first Jp app!", classes='text-green-600')
    jp.Div(a=div1, text="Trial elements", 
            classes='border border-black text-green-600 hover:bg-blue-500 hover:text-white px-2',
            mouseenter=mouse_in, mouseleave=mouse_out)
    
    div2 = jp.Div(a=dad, classes='grid grid-cols-2 gap-6 justify-items-center')
    d_out = jp.Div(a=div2, text="Second div", classes='text-red-600 font-bold')
    jp.Button(a=div2 , text="press ME !", inp1=inp1, inp2=inp2, d_out=d_out, click=summation,
            classes='border-4 border-blue-400 rounded w-1/2'
                    ' hover:bg-white hover:text-red-400 hover:border-yellow-400')
    
    return wp

def summation(widget, msg):
    summ = float(widget.inp1.value) + float(widget.inp2.value)
    widget.d_out.text = summ

#*2
def mouse_in(widget, msg):
    widget.text = 'Aoooch!'

def mouse_out(widget, msg):
    widget.text = 'Oooh yeah'

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
-------
## GETTING INPUT FROM INPUT ELEMENT & USING ITS VALUE IN CODE ##
1- First define a function to handle this event; which is called event handler (not request handler)
2- This func accepts 2 args; widget and msg;
    - widget refers to the widget initialized the event, and contains its attributes.
    - msg is a dict containing info about event attributes, like type:click, page:webpage and so.
3- Declare a variable name for each input used by the widget, then inside Button; add an attr for
each input with its name (<inp_attr=<inp_var>)
- As mentioned earlier, widget arg refers to the widget. So we can simply use widget.inp_var to 
refer to that input. To get the exact value entered by user use widget.inp_var.value

- Same idea for showing an output on a div for instance; we define it in the Button widget, 
change its attribute value in our event handler to what we want.
- Again, same thing applies for mouse going out of div :)

#*2
hover controls styling of a widget when the mouse enters its area, However if we need to manipulate
far more than just the styling (like text), we'll have to define a separate function.

#* You can see all Tailwind attributes and values from here: https://tailwindcss.com/docs/installation

#*3
wp = jp.WebPage()
- Using WebPage object enables you to use tailwind properties for your widgets, However, There's 
another framework QuasarPage which has more advanced features. You can see the docs here:
* https://quasar.dev/docs
- With Quasar; You should use its widgets, for instance Button is QBtn and so..
- If you still want to use tailwind properties with this framework, enable tailwind to True:
wp = jp.QuasarPage(tailwind=True)

"""