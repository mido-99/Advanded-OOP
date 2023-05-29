from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file(filename="search.kv")

class FirstScreen(Screen):
    def search_images(self):
        pass

class RootWidget(ScreenManager):
    pass

class SearchApp(App):
    def build(self):
        return RootWidget()
    
SearchApp().run()


'''
## Steps for creating app using kivy ##

# Python Script #
1. First there's a MainApp class -or call it <anything>App; this class inherits from (App) class that is imported from kivy.app. So it's like the template on which we build our app.
- Inside this class we'll overwrite build(self) method to return the ScreenManager object that we have defined (see point 2).
2. Define a RootWidget class; this class inherits from (ScreenManager) imported from kivy.uix.screenmanager. 
It's like a manager for any other Screen object we'll create later (a screen object for each new screen in the app).
3. Define a Screen object that inherts from (Screen); This is the screen object we're talking about, on which we'll put layouts and widgets. And also define the methods that these widgets will execute.
4. Run the app: MainApp().run()
5. To connect script to .kv file:
- By default, Kivy expects the .kv file to have the same base name as your Python file. For example, if your Python file is named myapp.py, the corresponding .kv file should be named myapp.kv.
- Alternatively, you can specify it manually this way:

from kivy.lang import Builder
Builder.load_file("filename.kv")


# .kv file for GUI #
In this file we will implement the GUI; screens, layouts, widgets and their attributes.

file start>>>
<Screen_name>:
    <Layout_type>:
        widget_1:
            attr_1: value
            attr_2: value
        widget_2:
            attr_1: value
......

<RootWidget>:
    Screen_name:
    id: id
    name: "name"

<<< file end

'''