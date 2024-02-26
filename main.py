from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from design2 import KV
import sqlite3
import hashlib


class MDTextFieldRound(MDTextField):
    pass


class Login(MDScreen):
    pass


class Registration(MDScreen):
    pass


class Menu(MDScreen):
    pass


class Myapp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        screens = [
            Login(),
            Registration(),
            Menu()
        ]
        for i in screens:
            sm.add_widget(i)
        return Builder.load_string(KV)

    def get_data(self):
        username = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text

    def get_data_registration(self):
        connection = sqlite3.connect('app.db')
        cursor = connection.cursor()
        username_r = self.root.get_screen('registration').ids.user_r.text
        password_r = self.root.get_screen('registration').ids.password_r.text
        psw_r = hashlib.sha256(password_r.encode()).hexdigest()
        result = cursor.execute(f"""INSERT INTO users(name, password) VALUES('{username_r}', '{psw_r}')""").fetchall()
        connection.commit()
        connection.close()



Myapp().run()
