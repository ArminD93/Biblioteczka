# File name: comiccreator.py
import kivy
kivy.require('1.7.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout



Builder.load_file('library.kv')
Builder.load_file('statusbar.kv')



class Biblioteczka(AnchorLayout):
    pass

class BiblioteczkaApp(App):
    def build(self):
        return Biblioteczka()

if __name__=="__main__":
    BiblioteczkaApp().run()
