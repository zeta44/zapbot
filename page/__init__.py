import os
from services import contact_service
import logging as log
from utilidadescev.crud import leiatxt, cadastro
from utilidadescev.dado import leiaInt, leiaStr
from utilidadescev.formatacao import cabecario, rodape
from time import sleep


def menu_principal():
    menu = ["Contacts", "Message", "Exit"]
    for i, v in enumerate(menu):
        print(f"{i + 1} - {v}")


def options_mp():
    while True:
        os.system("cls") or None
        cabecario('Whatsapp Automatic')
        menu_principal()
        rodape()
        option = leiaInt('Select an option: ')
        sleep(0.5)

        if option == 1:
            os.system("cls") or None
            cabecario('Contacts Options')
            menu = ["Read", "Create", "Delete", "Back"]
            for i, v in enumerate(menu):
                print(f"{i + 1} - {v}")
            rodape()

            while True:
                option = leiaInt("Select an option: ")
                if option == 1:
                    print(menu[0])
                    contact_service.edit_contacts("r")
                    continue
                if option == 2:
                    print(f"{menu[1]} - (Type 'Exit' to leave.)")
                    nome = str(input("Type Contact or Group name: "))
                    if nome in "ExitexitEXIT":
                        break
                    else:
                        contact_service.edit_contacts("c", nome)
                        continue
                if option == 3:
                    print(f"{menu[2]} - (Type 'Exit' to leave.)")
                    nome = str(input("Type Contact or Group name: "))
                    if nome in "ExitexitEXIT":
                        break
                    else:
                        contact_service.edit_contacts("d", nome)
                        continue
                if option == 4:
                    break

                else:
                    log.info("Invalid option.")

            continue
        elif option == 2:
            break

        elif option == 3:
            print('SHUTTING DOWN...')
            exit()
            break

        else:
            print('Invalid Option!!!!')
            continue
