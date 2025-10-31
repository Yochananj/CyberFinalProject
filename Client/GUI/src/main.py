import logging
import os
import flet as ft

from Client.GUI.src.Controllers.HomeController import HomeController
from Client.GUI.src.Controllers.LoginController import LoginController
from Client.GUI.src.Views.HomeView import HomeView
from Client.GUI.src.Views.LoginView import LoginView
from Client.GUI.src.Controllers.SignUpController import SignUpController
from Client.GUI.src.Views.ViewsAndRoutesList import ViewsAndRoutesList
from Client.GUI.src.Views.SignUpView import SignUpView
from Dependencies.Constants import crypt_drive_blue


class GUI:
    def __init__(self, page: ft.Page):
        self.top_view = None
        self.controller = None

        self.page = page
        self.page.window.width = 600
        self.page.window.height = 600

        self.page.theme = ft.Theme(color_scheme_seed=crypt_drive_blue)

        self.page.fonts = {
            "Aeonik": f"{os.path.dirname(os.path.dirname(__file__))}/assets/Aeonik/AeonikExtendedLatinHebrew-Regular.otf",
            "Aeonik Bold": f"{os.path.dirname(os.path.dirname(__file__))}/assets/Aeonik/AeonikExtendedLatinHebrew-Bold.otf",
            "Aeonik Black": f"{os.path.dirname(os.path.dirname(__file__))}/assets/Aeonik/AeonikExtendedLatinHebrew-Black.otf",
            "Aeonik Thin": f"{os.path.dirname(os.path.dirname(__file__))}/assets/Aeonik/AeonikExtendedLatinHebrew-Thin.otf"

        }

        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.themeMode = "light"
        self.page.window.on_resize = self.upon_window_size_change

        self.navigator(ViewsAndRoutesList.LOG_IN)


    def upon_window_size_change(self):
        self.page.update()

    def navigator(self, to_page: ViewsAndRoutesList, username: str = None, password: str = None):
        self.page.clean()

        match to_page:
            case ViewsAndRoutesList.LOG_IN:
                self.page.title = "CryptDrive: Log In"
                self.page.views.clear()
                self.top_view = LoginView(username_start_value=username, password_start_value=password)
                self.page.views.append(self.top_view.build())
                self.controller = LoginController(page=self.page, view=self.top_view, navigator=self.navigator)
            case ViewsAndRoutesList.SIGN_UP:
                self.page.title = "CryptDrive: Sign Up"
                self.page.views.clear()
                self.top_view = SignUpView(username_start_value=username, password_start_value=password)
                self.page.views.append(self.top_view.build())
                self.controller = SignUpController(page=self.page, view=self.top_view, navigator=self.navigator)
            case ViewsAndRoutesList.HOME:
                self.page.title = "CryptDrive: Home - Files"
                self.page.views.clear()
                self.top_view = HomeView(self.page.window.height)
                self.page.views.append(self.top_view.build())
                self.controller = HomeController(page=self.page, view=self.top_view, navigator=self.navigator)
            case _:
                logging.error("Invalid page.")

        self.page.update()



if __name__ == "__main__":
    ft.app(GUI)




