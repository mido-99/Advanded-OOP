from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock, time

# from filesharer import FileSharer

Builder.load_file("frontend.kv")

class VidScreen(Screen):

    def record(self):
        # start recording, change background to red
        self.ids.camera.play = True
        self.ids.record_btn.background_color = (100, 0, 0, 1)
        self.ids.record_btn.text = "Stop"
        
    def stop(self):
        # stop recording, change background to normal, set frame to black
        self.ids.camera.play = False
        self.ids.record_btn.background_color = (1, 1, 1, 1)
        self.ids.camera.texture = None
        self.ids.record_btn.text = "Start Recording"
        
    def capture(self):
        # capture frame with current time, reset btn text to original
        self.ids.cap_btn.text = "Captured!"
        curr_time = time.strftime("%Y-%m-%d_%H;%M;%S")
        img_path = f"output\{curr_time}.png" 
        self.ids.camera.export_to_png(img_path)
        Clock.schedule_once(lambda dt : setattr(self.ids.cap_btn, 'text', "Capture image"), 1)
        # Switch to anothe Screen:
        self.manager.current = "img_screen" #*
        return img_path

class ImgScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        Window.size = (Window.width * 0.7, Window.height * 0.8)
        return RootWidget()

MainApp().run()


"""
#########################################################
#* NOTE that in screen switching; we use screen NAME. NOT id and not class

"""