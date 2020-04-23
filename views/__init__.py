import os
from services import contact_service
from utils.dado import leiaInt
from utils.formatacao import cabecario, rodape
from time import sleep
import logging


class MenuView:

    def __init__(self):
        logging.debug('Loaded menu class')

    def render(self):
        """
        Renders the menu
        """
        os.system("cls") or None
        cabecario('Whatsapp Automatic')
        menu = ["Contacts", "Message", "Exit"]
        for i, v in enumerate(menu):
            print(f"{i + 1} - {v}")
        rodape()
        option = leiaInt('Select an option: ')
        sleep(0.5)

        if option == 1:
            return ContactMenuView().render()
        elif option == 2:
            return MessagesMenuView().render()
        elif option == 3:
            return True
        else:
            logging.info("Invalid option.")


class ContactMenuView:
    def __init__(self):
        logging.debug('Creating contact menu')

    def render(self):
        logging.debug('Rendering contact menu')

        os.system("cls") or None
        cabecario('Contacts Options')
        menu = ["Read", "Create", "Delete", "Back"]
        for i, v in enumerate(menu):
            print(f"{i + 1} - {v}")
        rodape()
        option = leiaInt("Select an option: ")
        if option == 1:
            print(menu[0])
            contact_service.edit_contacts("r")
            return self.render()
        if option == 2:
            nome = str(input("Type Contact or Group name: "))
            contact_service.edit_contacts("c", nome)
            return self.render()
        if option == 3:
            nome = str(input("Type Contact or Group name: "))
            contact_service.edit_contacts("d", nome)
            return self.render()
        if option == 4:
            return False


class MessagesMenuView:
    def __init__(self):
        logging.debug('Creating messages menu')

    def render(self):
        logging.warning('Method MessagesMenuView.render() is not implemented')
        # TODO: Add the logic to read a text message and send it