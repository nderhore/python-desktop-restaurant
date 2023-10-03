from PyQt6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QDialog

import controller.client as client_controller
from ihm.ClientDialog import ClientDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservation Restaurant")
        self.setGeometry(100, 100, 400, 300)

        # definition de ma liste de client
        self.client_list = QListWidget(self)

        # alimentation de la liste
        self.button_add_client = QPushButton("Ajouter un client")
        self.button_add_client.clicked.connect(self.open_dialog_create_client)

        layout = QVBoxLayout()
        layout.addWidget(self.client_list)
        layout.addWidget(self.button_add_client)
        self.setLayout(layout)

    def open_dialog_create_client(self):
        dialog = ClientDialog()
        dialog.accepted.connect(self.refresh_list)
        dialog.exec()

    def refresh_list(self):
        self.client_list.clear()
        client_list_db = client_controller.get_all_client()
        for client in client_list_db:
            self.client_list.addItem(client.prenom + " " + client.nom)
