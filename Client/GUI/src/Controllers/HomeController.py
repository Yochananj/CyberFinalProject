from tokenize import blank_re

import flet as ft

from Client.GUI.src.Views.AccountContainer import AccountContainer
from Client.GUI.src.Views.FilesContainer import FilesContainer
from Client.GUI.src.Views.HomeView import HomeView
from Client.GUI.src.Views.SettingsContainer import SettingsContainer


class HomeController:
    def __init__(self, page: ft.Page, view: HomeView, navigator):
        self.view = view
        self.navigator = navigator
        self.page = page

        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment = "center"
        self.page.update()
        self.mini_navigator()
        self.attach_handlers()

    def attach_handlers(self):
        self.view.nav_rail.on_change = self.mini_navigator


    def mini_navigator(self, control_event=None):
        print("switched to destination", self.view.nav_rail.selected_index)
        print(control_event)
        match self.view.nav_rail.selected_index:
            case 0:
                self.page.title = "CryptDrive: Home - Files"
                self.view.body.content = FilesContainer().build()
                self.page.update()
            case 1:
                self.page.title = "CryptDrive: Home - Account"
                self.view.body.content = AccountContainer().build()
                self.page.update()
            case 2:
                self.page.title = "CryptDrive: Home - Settings"
                self.view.body.content = SettingsContainer().build()
                self.page.update()