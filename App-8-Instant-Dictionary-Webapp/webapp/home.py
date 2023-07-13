import justpy as jp

class Home():
    path = '/'
    
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        dad = jp.Div(a= wp, classes='bg-gray-200 h-screen text-lg p-8')
        
        div1 = jp.Div(a= dad, text='This is a       Home page', classes='text-3xl')
        div2 = jp.Div(a= dad, text='This is bigger div ', classes='text-6xl')
        
        return wp
