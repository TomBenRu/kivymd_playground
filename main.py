from kivymd.app import MDApp
from kivymd.uix.card import MDCard


class LoginScreen(MDCard):

    def login(self):
        self.ids.welcome_label.text = f"Welcome {self.ids.user.text}"

    def clear(self):
        self.ids.welcome_label.text = "Welcome"
        self.ids.user.text = ""
        self.ids.password.text = ""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return LoginScreen()


MainApp().run()
