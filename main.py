from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard


class LoginScreen(MDCard):

    def login(self):
        self.root.ids.welcome_label.text = f"Welcome {self.root.ids.user.text}"

    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return LoginScreen()



MainApp().run()
