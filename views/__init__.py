import os
from utils.data import leiaInt, leiaStr
from utils.formatter import cabecario, rodape
from time import sleep
import logging
from services import ContactService, MessageService


class MenuView:
    contactmenuview = None
    messagesmenuview = None


    def __init__(self):
        logging.debug('Loaded menu class')
        self.contactmenuview = ContactMenuView()
        self.messagesmenuview = MessagesMenuView()

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
            return self.contactmenuview.render()
        elif option == 2:
            return self.messagesmenuview.render()
        elif option == 3:
            return True
        else:
            logging.info("Invalid option.")

    def destroy_main_menu(self):
        self.messagesmenuview.destroy_message_menu()


class ContactMenuView:

    contact_service = None
    def __init__(self):
        logging.debug('Creating contact menu')
        self.contact_service = ContactService()

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
            self.contact_service.edit_contacts("r")
            input("Press enter to continue...")
            return self.render()
        if option == 2:
            print(menu[1])
            self.contact_service.edit_contacts("r")
            nome = str(input("Type Contact or Group name to Create: "))
            quest = input("Confirm [Y - N]: ")
            if quest in "yY" and quest != "":
                self.contact_service.edit_contacts("c", nome)
                self.contact_service.edit_contacts("r")
                input("Press enter to continue...")
                return self.render()
            if quest in "nN":
                print("Action discarded.")
                self.contact_service.edit_contacts("r")
                input("Press enter to continue...")
                return self.render()
            else:
                print("Action discarded.")
                self.contact_service.edit_contacts("r")
                input("Press enter to continue...")
                return self.render()

        if option == 3:
            print(menu[2])
            self.contact_service.edit_contacts("r")
            nome = str(input("Type Contact or Group name to Delete: "))
            quest = input("Confirm [Y - N]: ")
            if quest in "yY" and quest != "":
                self.contact_service.edit_contacts("d", nome)
                self.contact_service.edit_contacts("r")
                input("Press enter to continue...")
                return self.render()
            if quest in "nN":
                print("Discarded.")
                self.contact_service.edit_contacts("r")
                input("Press enter to continue...")
                return self.render()
            else:
                print("Discarded.")
                self.contact_service.edit_contacts("r")
                input("Press enter to continue...")
                return self.render()

        if option == 4:
            return False


class MessagesMenuView:

    messageService = None

    def __init__(self):
        logging.debug('Creating messages menu')
        if not self.messageService:
            self.messageService = MessageService()
            self.messageService.init_driver()

    def render(self):
        logging.warning('Method MessagesMenuView.render() is not implemented')
        # TODO: Add the logic to read a text message and send it
        self.message = []


        # self.messageService = MessageService()
        #
        cabecario("Whatsapp Auto Menssager")

        quest = input("Do you want to send a message? [Y - N]: ")

        if quest in "YyNn" and quest != "":
            if quest in "Yy":
                cabecario("Menssagem")
                rodape()
                text = leiaStr("Type your message: ")
                self.message.append(text)

                print("Wait a moment...")
                sleep(2)
                if len(self.message) > 0:
                    self.messageService.send_text_message(self.message)
                    return False

            elif quest in "Nn":
                return False

        else:
            print("Answer Y or N !")
            return self.render()

    def destroy_message_menu(self):
        self.messageService.destroy_driver()