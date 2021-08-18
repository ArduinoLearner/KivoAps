from kivy.lang import Builder
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

#Color a los widgets
from kivy.utils import get_color_from_hex

#Color de fondo
from kivy.core.window import Window
#Definir color de fondo
Window.clearcolor = get_color_from_hex(("#3737C4"))


#from kivy.app import App
#import kivy
#kivy.require ('1.11.0')



code = """
<LeButton@Button>:
    text: ""
    on_press: app.escritura(str(self.text)) #Si la funcion a llamar fuera declarada dentro de una clase diferente sería root.función Pero está dentro de la clase App 
    background_color: ("#656599")
    background_normal: ""
    font_size: '45sp'


BoxLayout:
    spacing: 20
    padding: 20
    orientation: 'vertical'

    TextInput: 
        size_hint_y: .4
        text:""
        id: lb
        font_size: '45sp'


    GridLayout:
        spacing: 10
        cols: 4
        
        LeButton:
            text: "1"

        LeButton:
            text: "2"
        
        LeButton:
            text: "3"
        
        LeButton:
            text: "+"
        
        LeButton:
            text: "4"

        LeButton:
            text: "5"
        
        LeButton:
            text: "6"
        
        LeButton:
            text: "-"
        
        LeButton:
            text: "7"

        LeButton:
            text: "8"
        
        LeButton:
            text: "9"
        
        LeButton:
            text: "/"
        
        LeButton:
            text: ""

        LeButton:
            text: "0"
        
        LeButton:
            text: "="
        
        LeButton:
            text: "*"
        
        
"""

class AptitudeApp(App):
    Le_cuenta = ""
    testo = ""
    
    def build (self):
        return Builder.load_string(code)
 
    def rut(self):
        #La ubicación del label está dentro de root asi que para acceder a ella
        self.root.ids.lb.text = "" #Si fuera declaración normal sin codigo dentro del mismo formato a python (kivy aparte) solo se llevaria self.ids.lb.text = ""
    
    
    def escritura(self,text):
        
        if(text == ""):
            AptitudeApp.Le_cuenta = AptitudeApp.Le_cuenta[:(len(AptitudeApp.Le_cuenta))-1]


        if (text != "="):
            pass
        
        AptitudeApp.Le_cuenta += text 

        self.root.ids.lb.text = AptitudeApp.Le_cuenta

        print(AptitudeApp.Le_cuenta)
        
                
                

        
      
  

AptitudeApp().run()
