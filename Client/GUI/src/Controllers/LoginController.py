import logging
import flet as ft
from Client.GUI.src.Views.LoginView import LoginView
from Client.GUI.src.Views.ViewsAndRoutesList import ViewsAndRoutesList


class LoginController:
    def __init__(self, page: ft.Page, view: LoginView, navigator):
        self.view = view
        self.navigator = navigator
        self.upon_text_field_change(page)
        self.attach_handlers(page)

    def attach_handlers(self, page: ft.Page):
        self.view.username.on_change = lambda e: self.upon_text_field_change(page)
        self.view.password.on_change = lambda e: self.upon_text_field_change(page)
        self.view.log_in_button.on_click = lambda e: self._upon_log_in_click(page)
        self.view.switch_to_sign_up_button.on_click = lambda e: self.upon_switch_to_sign_up_click(page)

    def upon_text_field_change(self, page: ft.Page):
        if self.view.username.value and self.view.password.value:
            self.view.log_in_button.disabled = False
        else:
            self.view.log_in_button.disabled = True
        page.update()

    def upon_switch_to_sign_up_click(self, page: ft.Page):
        current_entry_username, current_entry_password = "", ""
        if self.view.username.value: current_entry_username = self.view.username.value
        if self.view.password.value: current_entry_password = self.view.password.value
        self.navigator(ViewsAndRoutesList.SIGN_UP, username=current_entry_username, password=current_entry_password)
        page.update()

    def _upon_log_in_click(self, page: ft.Page):
        print("Log In clicked")
        self.navigator(ViewsAndRoutesList.HOME)