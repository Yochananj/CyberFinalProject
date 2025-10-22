import logging
import flet as ft
from Client.GUI.src.Controllers.LoginController import LoginController
from Client.GUI.src.Pages.LoginPage import LoginPage
from Client.GUI.src.Controllers.SignUpController import SignUpController
from Client.GUI.src.Pages.SignUpPage import SignUpPage

class GUI:
    def __init__(self, page: ft.Page):
        logging.Filter("debug")
        self.view = None
        self.controller = None

        self.page = page
        self.page.window.width = 600
        self.page.window.height = 600
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.themeMode = ft.ThemeMode.LIGHT

        self.navigator("Log In")

    def navigator(self, to_page: str, username: str = None, password: str = None):
        self.page.clean()

        match to_page:
            case "Log In":
                self.view = LoginPage(start_username_with=username, start_password_with=password)
                self.page.add(self.view.build())
                self.controller = LoginController(page=self.page, view=self.view, navigator=self.navigator)
            case "Sign Up":
                self.view = SignUpPage(start_username_with=username, start_password_with=password)
                self.page.add(self.view.build())
                self.controller = SignUpController(page=self.page ,view=self.view, navigator=self.navigator)
            case _:
                logging.error("Invalid page.")

        self.page.update()







if __name__ == "__main__":
    ft.app(GUI)





































#
# def main(page: ft.Page):
#     # Window definitions
#     page.title = "Sign Up / Log In"
#     page.window.width = 600
#     page.window.height = 600
#     page.window.resizable = False
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.LIGHT
#
#     # Login Objects
#     text_username: TextField = TextField(label="Username", text_align=ft.TextAlign.LEFT, width=300)
#     text_password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=300, password=True)
#     text_password_confirmation: TextField = TextField(label="Password Confirmation", text_align=ft.TextAlign.LEFT,
#                                                       width=300, password=True)
#
#     checkbox_sign_up: Checkbox = Checkbox(label="Sign Up", value=False)
#     button_log_in: ElevatedButton = ElevatedButton(text="Log In", width=300, disabled=True)
#
#
#     # Alert Section
#     def ok_button(e: ControlEvent):
#         page.remove(alert_dialog)
#         page.update()
#
#     alert_button = Button(text="OK", on_click=ok_button)
#
#     alert_dialog = ft.AlertDialog(
#         modal=True,
#         title=Text(value="Password confirmation doesn't match Password"),
#         content=Text(value="Please try again."),
#         actions=[alert_button],
#         actions_alignment=ft.MainAxisAlignment.END
#     )
#
#
#     # Login Page Setup
#     def sign_up_page():
#         page.clean()
#         checkbox_sign_up.value = True
#         button_log_in.text = "Sign Up"
#         page.add(
#             Row(
#                 controls=[Column([
#                     text_username,
#                     text_password,
#                     text_password_confirmation,
#                     checkbox_sign_up,
#                     button_log_in]
#                 )],
#                 alignment=ft.MainAxisAlignment.CENTER
#             )
#         )
#         page.update()
#
#     def log_in_page():
#         page.clean()
#         checkbox_sign_up.value = False
#         button_log_in.text = "Log In"
#         page.add(
#             Row(
#                 controls=[Column([
#                     text_username,
#                     text_password,
#                     checkbox_sign_up,
#                     button_log_in]
#                 )],
#                 alignment=ft.MainAxisAlignment.CENTER
#             )
#         )
#         page.update()
#
#     def validate(e: ControlEvent):
#         if all([text_username.value, text_password.value, text_password_confirmation.value]): # if all have values
#             button_log_in.disabled = False
#         else:
#             button_log_in.disabled = True
#
#         page.update()
#
#     def submit(e: ControlEvent):
#         print("Submit Clicked")
#         if text_password.value == text_password_confirmation.value:
#             print(f"Username: {text_username.value}")
#             print(f"Password: {text_password.value}")
#
#             page.clean()
#             page.add(
#                 Row(controls=[
#                      Text(value=f"Welcome, {text_username.value}!",
#                           text_align=ft.TextAlign.CENTER)
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER
#                 )
#             )
#             page.update()
#         else:
#             page.dialog = alert_dialog
#             page.update()
#
#     def switch_pages(e: ControlEvent):
#         if checkbox_sign_up.value:
#             sign_up_page()
#         else:
#             log_in_page()
#
#     # Event Handling
#     text_username.on_change = validate
#     text_password.on_change = validate
#     text_password_confirmation.on_change = validate
#
#     checkbox_sign_up.on_change = switch_pages
#     button_log_in.on_click = submit
#
#     log_in_page()
#
# ft.app(main)

