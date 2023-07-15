import justpy as jp

from webapp.home import Home
from webapp.about import About

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)

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

"""