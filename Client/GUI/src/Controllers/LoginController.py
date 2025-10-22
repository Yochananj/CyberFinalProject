import flet as ft
from Client.GUI.src.Pages.LoginPage import LoginPage


class LoginController:
    def __init__(self, page: ft.Page):
        self.view = LoginPage()
        self.attach_handlers(page)

    def attach_handlers(self, page: ft.Page):
        self.view.username.on_change = lambda e: self._upon_text_field_change(page)
        self.view.password.on_change = lambda e: self._upon_text_field_change(page)
        self.view.log_in_button.on_click = lambda e: self._upon_log_in_click(page)

    def _upon_text_field_change(self, page: ft.Page):
        if self.view.username.value and self.view.password.value:
            self.view.log_in_button.disabled = False
        else:
            self.view.log_in_button.disabled = True
        page.update()


    def _upon_log_in_click(self, page: ft.Page):
        pass