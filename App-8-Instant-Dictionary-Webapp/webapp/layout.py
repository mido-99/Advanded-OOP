import justpy as jp

class LayoutDefault(jp.QLayout):
    
    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)
        
        header = jp.QHeader(elevated=True, a=self) #*
        toolbar = jp.QToolbar(a=header, classes='bg-green-500')
        
        drawer = jp.QDrawer(a=self,
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
        jp.A(a=qlist, href='/contact', text='Contact us', classes= nav_a_classees)
        jp.Br(a=qlist)
        
        jp.QBtn(dense=True, flat=True, round=True, icon="menu",
                            click=self.move_drawer, a=toolbar, drawer=drawer)
        jp.QToolbarTitle(text="Instant Dictionary", a=toolbar)
    
    @staticmethod
    def move_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value

"""
In the non-class version of this part of code; we wrote a=layout, as it was defined as a separate
variable. But here its replaced by self since self is actually the layout (instance of Layout)

#! classes='fit' is very important, Unless it; nothing is gonna appear
"""