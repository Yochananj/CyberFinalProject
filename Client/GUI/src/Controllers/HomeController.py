import json
import logging

import flet as ft

from Client.GUI.src.Views.AccountContainer import AccountContainer
from Client.GUI.src.Views.FilesContainer import FilesContainer, FileTile, FolderTile
from Client.GUI.src.Views.HomeView import HomeView
from Client.GUI.src.Views.SettingsContainer import SettingsContainer
from Client.GUI.src.Views.ViewsAndRoutesList import ViewsAndRoutesList
from Dependencies.Constants import crypt_drive_blue, crypt_drive_theme, crypt_drive_fonts
from Dependencies.VerbDictionary import Verbs


class HomeController:
    def __init__(self, page: ft.Page, view: HomeView, navigator, comms_manager):
        self.view = view
        self.navigator = navigator
        self.comms_manager = comms_manager
        self.page = page
        self.page.theme = crypt_drive_theme
        self.container = None
        self.current_dir = "/"

        self.page.fonts = crypt_drive_fonts

        self.page.views[0].floating_action_button_location = ft.FloatingActionButtonLocation.START_FLOAT
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.file_container = FilesContainer()
        self.account_container = AccountContainer()
        self.settings_container = SettingsContainer()

        self.mini_navigator()
        self.attach_handlers()

    def attach_handlers(self):
        self.view.nav_rail.on_change = self.mini_navigator
        self.attach_handlers_per_destination()

    def attach_handlers_per_destination(self):
        match self.view.nav_rail.selected_index:
            case 0:  # Files container
                pass

            case 1:  # Account container
                self.account_container.log_out_button.on_click = lambda e: self.log_out()

            case 2:  # Settings container
                pass

    def get_file_list(self):
        logging.debug("Getting file list")
        status, dirs_and_files = self.comms_manager.send_message(verb=Verbs.GET_FILES_LIST, data=[self.current_dir])
        dirs, files = [], []


        logging.debug(f"status: {status}")
        logging.debug(f"dirs_and_files: <{dirs_and_files}>, type: {type(dirs_and_files)}")
        logging.debug(f"dirs_and_files[0]: {dirs_and_files[0]}")


        if dirs_and_files[0]:
            dirs, files = json.loads(dirs_and_files[0]), json.loads(dirs_and_files[1])

        return dirs, files

    def log_out(self):
        self.navigator(ViewsAndRoutesList.LOG_IN)
        self.comms_manager.token = 'no_token'

    def mini_navigator(self, control_event=None):
        logging.debug(f"switched to destination: {self.view.nav_rail.selected_index}")
        logging.debug(control_event)

        match self.view.nav_rail.selected_index:
            case 0:  # Files container
                self.page.title = "CryptDrive: Files"
                self.container = self.file_container

                self.container.column.controls.clear()
                self.container.column.controls.append(self.container.title)


                if self.current_dir is "/": self.container.column.controls.append(FolderTile(folder_name="", item_count=None, is_current_directory=True, path=self.current_dir, root=True).tile)
                else: self.container.column.controls.append(FolderTile(folder_name=self.current_dir.split("/")[-1], item_count=None, is_current_directory=True, path=self.current_dir[0:len(self.current_dir) - len(self.current_dir.split("/")[-1])]).tile)


                dir_list, file_list = self.get_file_list()
                for directory in dir_list:
                    self.container.column.controls.append(
                        FolderTile(
                            folder_name=directory["path"].split("/")[-1],
                            item_count=directory["item_count"]
                        ).tile
                    )
                for file in file_list:
                    self.container.column.controls.append(
                        FileTile(
                            file_name=file["name"],
                            file_size=file["size"]
                        ).tile
                    )

            case 1:  # Account container
                self.page.title = "CryptDrive: Account"
                self.container = self.account_container

            case 2:  # Settings container
                self.page.title = "CryptDrive: Settings"
                self.container = self.settings_container

        self.view.body.content = self.container.build()
        self.container.title.font_family = "Aeonik Black"
        self.container.title.size = 90
        self.container.title.color = crypt_drive_blue
        self.container.column.scroll = True
        self.container.column.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.attach_handlers_per_destination()

        if self.view.nav_rail.selected_index == 0:
            self.page.views[0].floating_action_button = self.container.fab
        else:
            self.page.views[0].floating_action_button = None
        self.page.update()
