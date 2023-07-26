import justpy as jp
from webapp import layout


class Contact():
    path = '/contact'
    
    @classmethod
    def serve(cls, req):
        # initialize webpage
        wp = jp.QuasarPage(tailwind=True)
        
        # Adding a default layout on which page content will be displayed
        lay = layout.LayoutDefault(a=wp)
        container = jp.QPageContainer(a=lay)
        
        # Page-specific content
        dad = jp.Div(a=container, classes='bg-gray-200 h-screen text-lg p-8')
        jp.Strong(a=dad, text='For Contact and Inquiries', classes='text-2xl')
        jp.P(a=dad, text='balblabalblab.bom ', classes='text-xl underline-offset-2')
        
        return wp
