from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from filesharer import FileSharer

Builder.load_file("frontend.kv")

class VidScreen(Screen):
    def record(self):
        pass
    def stop(self):
        pass
    def capture(self):
        pass
    pass

class CamScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp.run()