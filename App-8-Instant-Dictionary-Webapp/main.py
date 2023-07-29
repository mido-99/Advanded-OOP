import inspect
import justpy as jp

from webapp import page
from webapp.home import Home
from webapp.about import About
from webapp.contact import Contact
from webapp.api import Api
from webapp.doc import Doc

imports = globals() #*

for webpage in list(imports.values()): #*2
    if hasattr(webpage, 'path') and hasattr(webpage, 'serve'):
        jp.Route(webpage.path, webpage.serve)

jp.justpy()

"""
When JustPy executes the passed serve method it doesn't intanimate an instance of this object;
it simply calls it as a #* class method: About.serve()
And as doing this will cause an error -since you can't call an inst method from a class you have
to create an instance of it- So justpy passes a request object to the serve().
- This way the request will be treated as self. And hence we reach the final poing that self
is not actually referring to our class! But to the passed request in this case.
- Which will give us just problems in case we need to refer to self.anything, thinking that we're
working with the class.
- The key to solve this issue is by using #* @classmethod
As mentioned above; we're calling the method from the class itself not an instance (inst is just
created when someone visits the webpage).

- Thought until now we've worked out half of the problem only, we still need that request object
in case we want to refer to it or its attrs, and to solve this it's really simple; just pass any
arbitrary var as second param for serve(cls, req) say req, and that's it!


#* globals Return the dictionary containing the current scope's global variables.
NOTE you have to explicitly import the pages classes earlier too

*2 What's going on here is that I'm trying to apply a filter on the modules imported by globals()
- This filter checks if it has a 'path' property (which is the case in our page objects).
As this  filter changes the dictionary size (cause not all modules in dict have path); 
it raises an error:  RuntimeError: dictionary changed size during iteration
- So to fix this we can either create a copy of our dict -so as loop isn't affected when filter
is applied- Or to create a list of dict values to achieve the same goal
>>> for value in list(imports.values()):
>>> for key, value in list(imports.copy()).items():

*3 AttributeError: 'SourceFileLoader' object has no attribute 'serve'
This is the error that will run into you when you try:
>>> if hasattr(value, 'path') and hasattr(value, 'serve'):
        jp.Route(value.path, value.serve)
-As some objects -Other than the page classes (here it's 'SourceFileLoader')- might have a path 
property; it may not be the best only filter to apply. So we need another one like:
>>> and hasattr(value, 'serve')
- Actually yes! a method is also treated as a attr for the obj (attrs are props and funcs)

### Final app 
import justpy as jp

from webapp.home import Home
from webapp.about import About
from webapp.contact import Contact

imports = globals() #*

for value in list(imports.values()): #*2

    if hasattr(value, 'path') and hasattr(value, 'serve'):
        jp.Route(value.path, value.serve)
###

#? Until this point, our app can run and work. But there's also another solution for this issue:
We create a new file in webpages classes' dir, give it arbitrary name say page.
We define a class Page(ABC) so it's just an abstract class with @abstractmethod serve()
This class is purposeless but to make each other webpage class inherit from so that we can apply 
the issubclass(value, page.Page) filter to filter them.
Also, we check if each value is a class to avoid  TypeError: issubclass() arg 1 must be a class
Lastly, we exclude page.Page itself as it's actually meet all the filters before

for value in list(imports.values()):
    if (
        inspect.isclass(value)
        and issubclass(value, page.Page)
        and value is not page.Page
    ):
        jp.Route(value.path, value.serve)

#? This is just another solution which can show us how to use Abstract methods and classes, 
#? you can use the first shorter one but this one is a good practice and better understand by other developers

"""