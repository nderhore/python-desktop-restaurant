from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import controller.client as client_controller
from entities.client import Client


class ClientDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create new client")

        self.lastname_label = QLabel("lastname : ")
        self.lastname_line = QLineEdit()

        self.firstname_label = QLabel("firstname : ")
        self.firstname_line = QLineEdit()

        self.gsm_label = QLabel("gsm : ")
        self.gsm_line = QLineEdit()

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_client)

        layout = QVBoxLayout()
        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_line)

        layout.addWidget(self.firstname_label)
        layout.addWidget(self.firstname_line)

        layout.addWidget(self.gsm_label)
        layout.addWidget(self.gsm_line)

        layout.addWidget(self.add_button)
        self.setLayout(layout)

    def add_client(self):
        firstname = self.firstname_line.text()
        lastname = self.lastname_line.text()
        gsm = self.gsm_line.text()
        client: Client = Client(nom=lastname, prenom=firstname, gsm=gsm)
        client_controller.create_client(client)
        self.accept()
