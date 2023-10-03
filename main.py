# This is a sample Python script.
import sys

from PyQt6.QtWidgets import QApplication, QWidget

from config.database import Base, engine, session
from entities.plat import Plat
from entities.categorie import Categorie
from entities.client import Client
from entities.cartePlat import CartePlat
from entities.carte import Carte
from entities.creneau import Creneau
from entities.reserver import Reserver
from entities.restaurantCreneau import RestaurantCreneau
from entities.restaurant import Restaurant
from ihm.MainWindow import MainWindow


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

    # Base.metadata.create_all(engine)
    # nouveau_restaurant = Restaurant(
#     capacite_max_midi=15,
#     capacite_max_soir=20,
#    horaire_midi="8h-12h",
#    horaire_soir="15h-18h",
# )
# session.add(nouveau_restaurant)
# session.commit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
