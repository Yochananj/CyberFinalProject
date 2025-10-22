import flet as ft
from flet import TextField, Row, Column, Checkbox, ElevatedButton, Text, Button
from flet_core import ControlEvent
from Client.GUI.src import main


class SignUpPage:
    def __init__(self, page: ft.Page):
        self.username = TextField(label="Username", text_align=ft.TextAlign.LEFT, width=300, autofocus=True)
        self.password = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=300, password=True)
        self.password_confirmation = TextField(label="Confirm Password", text_align=ft.TextAlign.LEFT, width=300, password=True)
        self.log_in_button = ElevatedButton(text="Sign Up", width=300, disabled=True)
        self.switch_to_log_in_button = ElevatedButton(text="Log In Instead", width=300, disabled=False)

        self.username.on_change = self.upon_text_field_change
        self.password.on_change = self.upon_text_field_change
        self.password_confirmation.on_change = self.upon_text_field_change

        self.switch_to_log_in_button.on_click = self.switch_to_login_page
        self.username.focus()

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



    def switch_to_login_page(self, page: ft.Page):
        pass

    def upon_text_field_change(self, page):
        if self.username.value and self.password.value and self.password_confirmation.value:
            self.log_in_button.disabled = False
        else:
            self.log_in_button.disabled = True
        page.update()




if __name__ == "__main__":
    ft.app(lambda page: SignUpPage(page))