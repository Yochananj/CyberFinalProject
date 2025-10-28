import flet as ft
from flet import TextField, Row, Column, Checkbox, ElevatedButton, Text, Button



class LoginPage:
    def __init__(self, username_start_value: str = "", password_start_value: str = ""):
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
                            self.username,
                            self.password,
                            self.log_in_button,
                            self.switch_to_sign_up_button]
                        )],
                    alignment=ft.MainAxisAlignment.CENTER)],
            can_pop=False,
            vertical_alignment=ft.MainAxisAlignment.CENTER
            )