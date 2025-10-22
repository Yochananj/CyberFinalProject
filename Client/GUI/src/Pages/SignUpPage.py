import flet as ft
from flet import TextField, Row, Column, Checkbox, ElevatedButton, Text, Button


class SignUpPage:
    def __init__(self, start_username_with: str = "", start_password_with: str = ""):
        self.username = TextField(value=start_username_with, label="Username", text_align=ft.TextAlign.LEFT, width=300, autofocus=True)
        self.password = TextField(value=start_password_with,label="Password", text_align=ft.TextAlign.LEFT, width=300, password=True)
        self.password_confirmation = TextField(label="Confirm Password", text_align=ft.TextAlign.LEFT, width=300, password=True)
        self.log_in_button = ElevatedButton(text="Sign Up", width=300, disabled=True)
        self.switch_to_log_in_button = ElevatedButton(text="Log In Instead", width=300, disabled=False)

    def build(self):
        return Row(
                controls=[Column([
                    self.username,
                    self.password,
                    self.password_confirmation,
                    self.log_in_button,
                    self.switch_to_log_in_button]
                )],
                alignment=ft.MainAxisAlignment.CENTER)


if __name__ == "__main__":
    pass