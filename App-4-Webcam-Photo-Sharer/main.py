from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
from urllib import request

Builder.load_file(filename="search.kv")

class FirstScreen(Screen):
    def get_img_link(self):
        # get user search
        query = self.manager.current_screen.ids.user_search.text
        # search wikipedia for user query
        page = wikipedia.page(query)
        img_link = page.images[0]
        img_path = f"images\wiki {query}.png"
        return img_link, img_path
    
    def download_wiki_img(self):
        img_link, img_path = self.get_img_link()
        img = request.urlretrieve(img_link, img_path)
        return img[0]
    
    def preview_img(self):
        # change images dynamically
        self.manager.current_screen.ids.img.source = self.download_wiki_img()  #*
        # self.ids.img.source = "images\git_init.png"  #= same above

class RootWidget(ScreenManager):
    pass

class SearchApp(App):
    def build(self):
        return RootWidget()
    
SearchApp().run()


'''
### Steps for creating app using kivy ###

## Python Script ##

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

6. To connect a method defined in your Screen object to a widget on that screen; say you have a button on that screen. Simply set on_press: root.method()     -like the example below-
- root here refers to the root widget of your widgets tree (which happens to be the screen object), that's why you should define that method in your Screen class declaration.
7. Get text from TextInput --> var = self.ids.<id>.text
NOTE It's a good practice to separate code in Screen class into several methods to ease its understanding and refactoring.


## .kv file for GUI ##

In this file we will implement the GUI; screens, layouts, widgets and their attributes.

file start>>>
<Screen_name>:
    <Layout_type>:
        widget_1:
            attr_1: value
            attr_2: value
        Button_1:
            on_press: root.method()
            
......

<RootWidget>:
    Screen_name:
    id: id
    name: "name"

<<< file end
______________________________________________________
#*
Let's break down the code:

- `self.manager`: `self` refers to the current instance of the class, and `manager` is a property or attribute of that instance. In this case, it is assumed that the current class has a `manager` attribute that represents a `ScreenManager` instance.

- `self.manager.current_screen`: `current_screen` is an attribute of the `ScreenManager` class that represents the currently displayed screen. By accessing `current_screen`, you are retrieving the instance of the currently active screen.

- `ids`: `ids` is a dictionary-like property of a widget that contains all the child widgets defined in the corresponding `.kv` file with an `id` attribute. The `id` attribute is used to uniquely identify a widget.

- `img`: `img` is the `id` assigned to an `Image` widget in the corresponding `.kv` file.

- `source`: `source` is a property of the `Image` widget that represents the path or URL of the image file to be displayed.

So, putting it all together, `self.manager.current_screen.ids.img.source = "images\image.png"` sets the `source` property of the `Image` widget (identified by the `id` "img") within the current screen of the `ScreenManager` to "images\image.png". It updates the image source, allowing you to change the displayed image dynamically.

'''