"""A doc for the api and how to use it"""

import justpy as jp
from webapp import layout
from webapp import page


class Doc(page.Page):
    path = '/doc'
    
    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        
        lay = layout.LayoutDefault(a=wp)
        container = jp.QPageContainer(a=lay)
        
        # Page-specific content
        dad = jp.Div(a=container, classes='bg-gray-200 h-screen text-lg p-8')
        jp.Div(a=dad, text='Get definition of words and terms', classes='text-3xl')
        jp.Div(a=dad, text='http://127.0.0.1:8000/api?w=boat', classes='text-lg')
        jp.Div(a=dad, text='''
            {'boat': ('A craft used for transportation of goods, fishing, racing, 
            recreational cruising, or military use on or in the water, propelled by oars or 
            outboard motor or inboard motor or by wind.', 
            'To traverse or travel by ship on a body of water.', 
            'A dish (often boat-shaped) for serving gravy or sauce.', 
            'A watercraft designed to float or plane on, and provide transport over water.')}''',
            classes='text-lg')
        
        return wp
