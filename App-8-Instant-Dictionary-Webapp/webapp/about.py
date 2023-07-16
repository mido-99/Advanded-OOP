import justpy as jp

class About():
    path = '/about'
    





    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        
        layout = jp.QLayout(view="hHh lpR fFf", a=wp)
        header = jp.QHeader(elevated=True, a=layout)
        toolbar = jp.QToolbar(a=header)
        
        drawer = jp.QDrawer(a=layout,
                            show_if_above=True, 
                            v_model="leftDrawerOpen",
                            bordered=True
                            )
        
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