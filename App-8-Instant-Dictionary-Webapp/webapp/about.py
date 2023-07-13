import justpy as jp

class About():
    path = '/about'
    
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        dad = jp.Div(a= wp, classes='bg-gray-200 h-screen text-lg p-8')
        
        div1 = jp.Div(a= dad, text='This is about page', classes='text-3xl')
        div2 = jp.Div(a= dad, text='This is bigger div ', classes='text-6xl')
        
        return wp
