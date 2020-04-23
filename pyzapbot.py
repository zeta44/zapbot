import logging
from views import MenuView

logging.basicConfig(level=logging.INFO)
logging.info('Starting pyzapbot')

while True:
    menuView = MenuView()
    if not menuView.render():
        continue
    else:
        break
