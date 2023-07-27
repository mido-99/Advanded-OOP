import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = '/about'
    
    @classmethod
    def serve(cls, req):
        # initialize webpage
        wp = jp.QuasarPage(tailwind=True)
        
        # Adding a default layout on which page content will be displayed
        lay = layout.LayoutDefault(a=wp)
        container = jp.QPageContainer(a=lay)
        
        # Page-specific content
        dad = jp.Div(a=container, classes='bg-gray-200 h-screen text-lg p-8')
        jp.Div(a=dad, text='This is about page', classes='text-3xl')
        jp.Div(a=dad, text='This is bigger div ', classes='text-6xl')
        
        return wp
