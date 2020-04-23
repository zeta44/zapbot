# TODO: Convert this file into a class and move it into the __init__.py

# Service that handles messages
from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
import logging as log
import os

driver = None


def init_driver():
    """
Start chromedriver.exe
    """
    global driver

    if driver is None:
        log.info("Start Driver, please wait...")
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        # On Google Chrome Type - chrome://version/ - So you can have the Profile path to save the browser configurations
        # You must change the final folder to store the exclusive settings for the program. In this case i create \\pybot after user data.
        # options.add_argument("user-data-dir=C:\\Users\\niger\\AppData\\Local\\Google\\Chrome\\User Data\\pybot")
        options.add_argument("user-data-dir=C:./browser")
        options.add_argument("utf8")
        # chromedriver.exe version 77....
        driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
        driver.get('https://web.whatsapp.com')
        sleep(20)
        log.info("Started driver")
    else:
        log.info("A driver is already available")


def dispose():
    global driver
    if not (driver is None):
        driver.close()
        driver.quit()
        driver = None
        log.info("Driver disposed")
    else:
        log.info("Driver already disposed")


def send_message(groups, message):
    global driver

    for group_or_person in groups:
        log.info(f'Sending message {message} to group {group_or_person}')

        # Não funcionou
        # search = driver.find_element_by_class_name("_39LWd")
        # sleep(1)
        # search.send_keys(group_or_person)

        group_field = driver.find_element_by_xpath(f"//span[@title='{group_or_person}']")
        sleep(1)
        group_field.click()
        chat_box = driver.find_element_by_class_name("_1Plpp")
        sleep(1)
        chat_box.click()
        chat_box.send_keys(message)
        send_button = driver.find_element_by_xpath("//span[@data-icon='send']")
        sleep(1)
        send_button.click()
        sleep(1)
    sleep(3)
    os.system("cls") or None


def is_driver_running():
    global driver
    return not (driver is None)
