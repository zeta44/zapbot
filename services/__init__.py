from selenium import webdriver
import logging as log
import os
from time import sleep



class ContactService:
    arquivo = ""

    def __init__(self):
        self.arquivo = "contacts.txt"

    def get_contacts(self):
        self.arquivo = "contacts.txt"
        groups_or_people = []
        contacts = open(self.arquivo, "r", encoding="utf8")
        conteudo = contacts.readlines()
        for i in range(len(conteudo)):
            linha = conteudo[i].strip("\n")
            groups_or_people.append(str(linha))
        contacts.close()
        return groups_or_people

    def edit_contacts(self, crud, name_contact=None):

        if crud == "c":
            contacts = open(self.arquivo, "r", encoding="utf8")
            conteudo = contacts.readlines()
            conteudo.append(name_contact + "\n")
            contacts = open(self.arquivo, "w", encoding="utf8")
            contacts.writelines(conteudo)
            contacts.close()
            log.info("Contato adicionado.")

        if crud == "r":
            groups_or_people = []
            contacts = open(self.arquivo, "r", encoding="utf8")
            conteudo = contacts.readlines()
            for i in range(len(conteudo)):
                linha = conteudo[i].strip("\n")
                groups_or_people.append(str(linha))
            contacts.close()
            log.info(groups_or_people)

        if crud == "d":
            contacts = open(self.arquivo, "r", encoding="utf8")
            conteudo = contacts.readlines()
            log.info(conteudo)
            conteudo.remove(name_contact + "\n")
            contacts = open(self.arquivo, "w", encoding="utf8")
            contacts.writelines(conteudo)
            contacts.close()
            log.info(f"Contact Deleted: {contacts}")


class MessageService:
    driver = None

    def __init__(self):
        global driver

    def init_driver(self):

        if not self.driver:
            log.info("Start Driver, please wait...")
            options = webdriver.ChromeOptions()
            options.add_argument("lang=pt-br")
            # On Google Chrome Type - chrome://version/ - So you can have the Profile path to save the browser configurations
            # You must change the final folder to store the exclusive settings for the program. In this case i create \\pybot after user data.
            # options.add_argument("user-data-dir=C:\\Users\\niger\\AppData\\Local\\Google\\Chrome\\User Data\\pybot")
            options.add_argument("user-data-dir=./browser")
            options.add_argument("utf8")
            # chromedriver.exe version 77....
            self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
            self.driver.get('https://web.whatsapp.com')
            log.info("Started driver")
        else:
            log.info("A driver is already available")

    def destroy_driver(self):
        global driver
        if not (self.driver is None):
            self.driver.close()
            self.driver.quit()
            self.driver = None
            log.info("Driver disposed")
        else:
            log.info("Driver already disposed")

    def send_text_message(self, message):
        groups = ContactService.get_contacts(self)
        for group_or_person in groups:
            log.info(f'Sending message {message} to group {group_or_person}')
            search_button = self.driver.find_element_by_xpath("//span[@data-icon='chat']")
            sleep(1)
            search_button.click()
            sleep(1)
            search_box = self.driver.switch_to.active_element
            sleep(1)
            search_box.send_keys(group_or_person)
            search_box.click()
            sleep(1)
            group_field = self.driver.find_element_by_xpath(f"//span[@title='{group_or_person}']")
            sleep(1)
            group_field.click()
            chat_box = self.driver.find_element_by_class_name("_1Plpp")
            sleep(1)
            chat_box.click()
            chat_box.send_keys(message)
            send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            sleep(1)
            send_button.click()
            sleep(1)
        sleep(3)
        os.system("cls") or None

    def is_driver_running(self):
        global driver
        return not (driver is None)
