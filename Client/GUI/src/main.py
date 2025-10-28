import logging
import flet as ft
from Client.GUI.src.Controllers.LoginController import LoginController
from Client.GUI.src.Views.LoginView import LoginPage
from Client.GUI.src.Controllers.SignUpController import SignUpController
from Client.GUI.src.Views.ViewsAndRoutesList import ViewsAndRoutesList
from Client.GUI.src.Views.SignUpView import SignUpPage

class GUI:
    def __init__(self, page: ft.Page):
        self.top_view = None
        self.controller = None

        self.page = page
        self.page.window.width = 600
        self.page.window.height = 600
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.themeMode = ft.ThemeMode.LIGHT

        self.navigator(ViewsAndRoutesList.LOG_IN)

    def navigator(self, to_page: ViewsAndRoutesList, username: str = None, password: str = None):
        self.page.clean()

        match to_page:
            case ViewsAndRoutesList.LOG_IN:
                self.page.views.clear()
                self.top_view = LoginPage(username_start_value=username, password_start_value=password)
                self.page.views.append(self.top_view.build())
                self.controller = LoginController(page=self.page, view=self.top_view, navigator=self.navigator)
            case ViewsAndRoutesList.SIGN_UP:
                self.page.views.clear()
                self.top_view = SignUpPage(username_start_value=username, password_start_value=password)
                self.page.views.append(self.top_view.build())
                self.controller = SignUpController(page=self.page, view=self.top_view, navigator=self.navigator)
            case _:
                logging.error("Invalid page.")

        self.page.update()



if __name__ == "__main__":
    ft.app(GUI)




