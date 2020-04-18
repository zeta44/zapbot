from selenium import webdriver
from time import sleep
import os


class WhatsappBot:
    def __init__(self):
        # Part 1 - The message you want to send
        self.message = []
        # Part 2 - Name of the groups or people you want to send the message to
        self.groups_or_people = ["Family Group", "Work Group"]

    def SendMessages(self):
        while True:
            os.system("cls") or None
            print("*=" * 12)
            print("   Whatsapp Automatic")
            print("*=" * 12)
            quest = str(input("Do you want to send a message? [Y - N]: "))
            os.system("cls") or None
            if quest in "YyNn":
                if quest in "Yy":
                    print("*=" * 12)
                    print("   Whatsapp Messager")
                    print("*=" * 12)
                    text = str(input("Type your message: "))
                    print("Wait a moment...")

                    if not hasattr(self, "driver"):
                        sleep(2)
                        options = webdriver.ChromeOptions()
                        options.add_argument("lang=pt-br")
                        # On Google Chrome Type - chrome://version/ - So you can have the Profile path to save the browser configurations
                        # You must change the final folder to store the exclusive settings for the program. In this case i create \\pybot after user data.
                        options.add_argument("user-data-dir=C:\\Users\\niger\\AppData\\Local\\Google\\Chrome\\User Data\\pybot")
                        #chromedriver.exe version 77....
                        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
                        self.driver.get('https://web.whatsapp.com')
                    self.message.append(text)
                    sleep(20)
                    if len(self.message) > 0:
                        for group_or_person in self.groups_or_people:
                            group_field = self.driver.find_element_by_xpath(
                                f"//span[@title='{group_or_person}']")
                            sleep(1)
                            group_field.click()
                            chat_box = self.driver.find_element_by_class_name("_1Plpp")
                            sleep(1)
                            chat_box.click()
                            chat_box.send_keys(self.message)
                            send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                            sleep(1)
                            send_button.click()
                            sleep(1)
                        self.message.clear()
                        print("Messages sent!")
                        sleep(3)
                        continue
                    else:
                        continue

                elif quest in "Nn":
                    print("Finalizando...")
                    if hasattr(self, "driver"):
                        self.driver.close()


                    break

            else:
                print("Answer Y or N !")


bot = WhatsappBot()
bot.SendMessages()


