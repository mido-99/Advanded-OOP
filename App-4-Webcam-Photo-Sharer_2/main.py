from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock, time
import webbrowser

from filesharer import FileSharer

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
        '''Create and save an image with current time as its name'''
        # capture frame with current time, reset btn text to original
        self.ids.cap_btn.text = "Captured!"
        curr_time = time.strftime("%Y-%m-%d_%H;%M;%S")
        self.img_path = f"output\{curr_time}.png" #****
        self.ids.camera.export_to_png(self.img_path)
        Clock.schedule_once(lambda dt : setattr(self.ids.cap_btn, 'text', "Capture image"), 1)
        
        # Switch to anothe Screen & add the image to its widget:
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "img_screen" #*
        self.manager.current_screen.ids.cap_image.source = self.img_path #**
        self.manager.current_screen.ids.label_link.text = ""

class ImgScreen(Screen):
    def create_link(self):
        '''Create a sharable link for the image and adds it to the label widget'''
        self.ids.label_link.text = "Hold on..."
        
        img_path = App.get_running_app().root.ids.vid_screen.img_path #***
        FileShare = FileSharer(img_path)
        self.url = FileShare.share()
        
        self.ids.label_link.text = self.url
        
    def copy_link(self):
        try: #*5
            Clipboard.copy(self.url)
        except:
            self.ids.label_link.text = "Create a link first!"

    def open_link(self):
        try:
            link = self.url
            webbrowser.open(link)
        except:
            self.ids.label_link.text = "Create a link first!"

        
    def go_back(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "vid_screen"

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

#*2 To set the image of a an image widget dynamically, we don't assign its value in the kv file, But instead after Screen switching (in the function). And note that here we're using manager.current_screen.ids... not self.ids directly; As self.ids is all about widgets of the current class in which methods are being defined.

#*3 root refers to the root widget of your app, hence you can access other children screens by ids

#*4 self is used to make it a class variable not just local for this method; so that I can retrieve this value later by just accessing theis instance.

#*5 Why we use try-except insteas of if statement: if we use if like this
if not self.url:
    self.ids.label_link.text = "Create a link first!"
else:
    Clipboard.copy(self.url)
#*5 The problem is that if user hasn't created a link yet; there's no actual self.url attr. so this error will be raised  AttributeError: 'ImgScreen' object has no attribute 'url'. Hence it should be handled using try-except.

"""