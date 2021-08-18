from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

#Color a los widgets
from kivy.utils import get_color_from_hex

#Color de fondo
from kivy.core.window import Window
#Definir color de fondo
Window.clearcolor = get_color_from_hex(("#3737C4"))


from kivy.app import App
import kivy
kivy.require ('1.11.0')



#Button.escritura = escritura


class MainScreen(BoxLayout):
    pass
 
    


class helloApp(App):
    def build(self):
        return MainScreen()
    
    def escritura(self,toxt):
        
        if(toxt == "c"):
            self.root.ids.lb.text = self.root.ids.lb.text[:int(len(self.root.ids.lb.text)-1)]

        if (toxt == "="):
            pass
        
        self.root.ids.lb.text += toxt.replace("c","") 



helloApp().run()
