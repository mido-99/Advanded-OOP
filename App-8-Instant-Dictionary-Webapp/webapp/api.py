import justpy as jp
import json

import definition

class Api():
    path = '/api'
    
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        defined = definition.Definition(word).get()
        
        resp = {
            word:defined
        }
        
        defined = json.dumps(resp)
        wp.html = resp
        
        return wp


"""
The idea about API is that now you have a service; an app, a webpage, any client whatever.
And someone comeswho wants to use this service, But they're using a different language.
Here comes the benefit of an api where apps can send requests and responses to each other
using json format data.

For example, the api takes the shape of this url: http://example.com?api_key=api_value
so ? to separate between api params

Let's take a look into the code above:
- First we define our req handler method which returns the wp object
- We then make use of the req itself, it has query_params prop which returns all the x=z in
the url. As we need only a particular query we use .get('query')

That's it! This way we have got the request from the client and we can process it or perform 
any operations this client needs, and then returns a response to them in json.
But how?

Well to do so, we are going to use json.dumps() which gets a dict as input:
- define a resp format like {word:def} or {'word':word, 'def':def}
- pass the dict as input for json.dumps(resp)

"""