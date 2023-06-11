from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

# from filesharer import FileSharer

Builder.load_file("frontend.kv")

class VidScreen(Screen):

    def record(self):
        self.ids.camera.play = True
        print(self.ids.record_btn.background_color)
        self.ids.record_btn.background_color = (100, 0, 0, 1)
        self.ids.record_btn.text = "Stop"
        
    def stop(self):
        self.ids.camera.play = False
        self.ids.record_btn.background_color = (1, 1, 1, 1)
        self.ids.camera.texture = None
        self.ids.record_btn.text = "Start Recording"

    def capture(self):
        pass

class CamScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        Window.size = (Window.width * 0.7, Window.height * 0.8)
        return RootWidget()

MainApp().run()
