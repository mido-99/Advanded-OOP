import justpy as jp

class About():
    path = '/about'
    
    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = jp.QLayout(view="hHh pR fFf", a=wp)
        header = jp.QHeader(elevated=True, a=layout)
        toolbar = jp.QToolbar(a=header, classes='bg-green-500')
        
        drawer = jp.QDrawer(a=layout,
                            show_if_above=True, 
                            v_model="leftDrawerOpen",
                            bordered=True,
                            width=120
                            )
        scroll = jp.QScrollArea(a=drawer, classes='fit') #!
        qlist = jp.QList(a=scroll, classes='pt-2')
        nav_a_classees = 'p-2 m-2 text-lg text-green-400 font-medium hover:text-green-600'
        jp.A(a=qlist, href='/', text='Home', classes= nav_a_classees)
        jp.Br(a=qlist)
        jp.A(a=qlist, href='/about', text='About', classes= nav_a_classees)
        jp.Br(a=qlist)
        
        jp.QBtn(dense=True, flat=True, round=True, icon="menu",
                            click=cls.move_drawer, a=toolbar, drawer=drawer)
        jp.QToolbarTitle(text="Instant Dictionary", a=toolbar)
        
        container = jp.QPageContainer(a=layout)
        dad = jp.Div(a=container, classes='bg-gray-200 h-screen text-lg p-8')
        jp.Div(a=dad, text='This is about page', classes='text-3xl')
        jp.Div(a=dad, text='This is bigger div ', classes='text-6xl')
        
        return wp
    
    @staticmethod
    def move_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value


"""
#! classes='fit' is very important, Unless it; nothing is gonna appear
"""