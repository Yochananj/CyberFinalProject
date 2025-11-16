import logging
import os
import sys
from pathlib import Path

from Client.Services.ClientFileService import FileService

# Ensure project root is on sys.path so 'Client' and 'Dependencies' can be imported
CURRENT_FILE = Path(__file__).resolve()
# For /.../CyberFinalProject/Client/GUI/src/main.py:
# CURRENT_FILE.parents[3] -> /.../CyberFinalProject (project root)
PROJECT_ROOT = CURRENT_FILE.parents[3]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import flet as ft
from Client.Services.ClientCommsManager import ClientClass
from Client.GUI.src.Controllers.HomeController import HomeController
from Client.GUI.src.Controllers.LoginController import LoginController
from Client.GUI.src.Controllers.SignUpController import SignUpController
from Client.GUI.src.Views.HomeView import HomeView
from Client.GUI.src.Views.LoginView import LoginView
from Client.GUI.src.Views.SignUpView import SignUpView
from Client.GUI.src.Views.ViewsAndRoutesList import ViewsAndRoutesList
from Dependencies.Constants import crypt_drive_fonts, crypt_drive_theme


class GUI:
    def __init__(self, page: ft.Page):
        self.top_view = None
        self.controller = None
        self.comms_manager = ClientClass()
        self.file_service = FileService()

        self.page = page
        self.page.window.icon = "window_icon.ico"
        self.page.window.width = 1200
        self.page.window.height = 900
        self.page.window.center()
        self.page.window.resizable = False

        self.page.fonts = crypt_drive_fonts
        self.page.theme = crypt_drive_theme

        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = "light"
        self.page.window.title_bar_hidden = True
        self.navigator(ViewsAndRoutesList.LOG_IN)


    def navigator(self, to_page: ViewsAndRoutesList, username: str = None, password: str = None):
        logging.info(f"Navigating to {to_page}")
        self.page.clean()

        match to_page:
            case ViewsAndRoutesList.LOG_IN:
                self.page.title = "CryptDrive: Log In"
                self.page.views.clear()
                self.top_view = LoginView(username_start_value=username, password_start_value=password)
                self.page.views.append(self.top_view.build())
                self.controller = LoginController(page=self.page, view=self.top_view, navigator=self.navigator, comms_manager=self.comms_manager)
            case ViewsAndRoutesList.SIGN_UP:
                self.page.title = "CryptDrive: Sign Up"
                self.page.views.clear()
                self.top_view = SignUpView(username_start_value=username, password_start_value=password)
                self.page.views.append(self.top_view.build())
                self.controller = SignUpController(page=self.page, view=self.top_view, navigator=self.navigator, comms_manager=self.comms_manager)
            case ViewsAndRoutesList.HOME:
                self.page.title = "CryptDrive: Home - Files"
                self.page.views.clear()
                self.top_view = HomeView(self.page.window.height, self.page.window.width)
                self.page.views.append(self.top_view.build())
                self.controller = HomeController(page=self.page, view=self.top_view, navigator=self.navigator, comms_manager=self.comms_manager, client_file_service=self.file_service)

        self.page.update()



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"{os.path.dirname(__file__)}/assets/window_icon.ico")
    ft.app(GUI, assets_dir="assets")




