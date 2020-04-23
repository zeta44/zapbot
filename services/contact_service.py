# Service that handles contacts
import logging as log

def get_contacts():
    groups_or_people = []
    contacts = open("contacts.txt", "r", encoding="utf8")
    conteudo = contacts.readlines()
    for i in range(len(conteudo)):
        linha = conteudo[i].strip("\n")
        groups_or_people.append(str(linha))
    contacts.close()
    return groups_or_people


def edit_contacts(crud, name_contact=None):

    if crud == "c":
        contacts = open("contacts.txt", "r", encoding="utf8")
        conteudo = contacts.readlines()
        conteudo.append(name_contact + "\n")
        contacts = open("contacts.txt", "w", encoding="utf8")
        contacts.writelines(conteudo)
        contacts.close()
        log.info("Contato adicionado.")

    if crud == "r":
        groups_or_people = []
        contacts = open("contacts.txt", "r", encoding="utf8")
        conteudo = contacts.readlines()
        for i in range(len(conteudo)):
            linha = conteudo[i].strip("\n")
            groups_or_people.append(str(linha))
        contacts.close()
        log.info(groups_or_people)

    if crud == "d":
        contacts = open("contacts.txt", "r", encoding="utf8")
        conteudo = contacts.readlines()
        log.info(conteudo)
        conteudo.remove(name_contact + "\n")
        contacts = open("contacts.txt", "w", encoding="utf8")
        contacts.writelines(conteudo)
        contacts.close()
        log.info(f"Contact Deleted: {contacts}")
        