import logging as log
from time import sleep
from services import contact_service
from services import message_service
import os
from page import options_mp


class WhatsappBot:
    def __init__(self):
        log.basicConfig(level=log.INFO, format='%(asctime)s %(message)s')
        options_mp()
        # Part 2 - Name of the groups or people you want to send the message to
        self.groups_or_people = contact_service.get_contacts()

    # controller, should only handle input and validation messages
    def SendMessages(self):
        while True:
            if not message_service.is_driver_running():
                p = "a"
            else:
                p = "another"
            print(f"Chosen groups or people: {self.groups_or_people}")
            quest = str(input(f"Do you want to send {p} message? [Y - N]: "))
            os.system("cls") or None
            if quest in "YyNn":
                if quest in "Yy":
                    print("*=" * 12)
                    print("   Whatsapp Messenger")
                    print("*=" * 12)
                    message = [str(input("Type your message: "))]
                    message_service.init_driver()

                    if len(message) > 0:
                        message_service.send_message(self.groups_or_people, message)
                        continue
                    else:
                        log.warning('Invalid message')
                        continue

                elif quest in "Nn":
                    print("Ending the program. Please wait...")
                    sleep(2)
                    message_service.dispose()
                    os.system("cls") or None
                    break

            else:
                print("Answer Y or N !")
                sleep(3)
                os.system("cls") or None


bot = WhatsappBot()
bot.SendMessages()
