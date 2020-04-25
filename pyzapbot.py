import logging
from views import MenuView

logging.basicConfig(level=logging.INFO)
logging.info('Starting pyzapbot')
menuView = MenuView()

while True:
    if not menuView.render():
        continue
    else:
        break

menuView.destroy_main_menu()