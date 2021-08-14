from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.app import App

from kivy.core.window import Window

from kivy.clock import Clock

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.graphics import Color, Rectangle

#Ventanas 
class RootWidget(FloatLayout):
    pass

class Screen1(BoxLayout):
    pass

class Screen2(BoxLayout):
    pass


class Screen3(BoxLayout):  
    @staticmethod
    def bish(self):   
        self.ids.lb.text = "B I S H"
        self.ids.lb.font_size = "45sp"
        with self.canvas.before:
            Color(1,0,0,0.60)
            self.rect = Rectangle(size=self.size, pos = self.pos)
        
        self.ids.bt.text = " U W U"        
        self.ids.bt.font_size = "45sp"

        
#Construcción 
class HelloApp(App):
    @staticmethod
    def build(self):
        return Screen2()
    @staticmethod
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()

#Correr
HelloApp().run()



