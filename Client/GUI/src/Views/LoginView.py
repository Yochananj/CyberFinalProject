import flet as ft
from flet import TextField, Row, Column, Checkbox, ElevatedButton, Text, Button
import os

from Dependencies.Constants import crypt_drive_blue


class LoginView:
    def __init__(self, username_start_value: str = "", password_start_value: str = ""):
        self.logo = Row(
            controls=[
                Column(width=30, controls=[ft.Text("")]),
                ft.Image(
                    src=os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/icon.png"),
                    width=200,
                    height=200,
                    fit=ft.ImageFit.FIT_WIDTH
                )]
        )
        self.username = TextField(value=username_start_value, label="Username", text_align=ft.TextAlign.LEFT, width=300, autofocus=True)
        self.password = TextField(value=password_start_value, label="Password", text_align=ft.TextAlign.LEFT, width=300, password=True)
        self.log_in_button = ElevatedButton(text="Log In", width=300, disabled=True)
        self.switch_to_sign_up_button = ElevatedButton(text="Sign Up Instead", width=300, disabled=False)

    def build(self):
        return ft.View(
            route = "/log_in",
            controls=[Row(
                    controls=[
                        Column([
                            self.logo,
                            self.username,
                            self.password,
                            self.log_in_button,
                            self.switch_to_sign_up_button]
                        )],
                    alignment=ft.MainAxisAlignment.CENTER)],
            can_pop=False,
            vertical_alignment=ft.MainAxisAlignment.CENTER
            )