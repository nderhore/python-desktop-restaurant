from config.database import session
from entities.client import Client


def create_client(client: Client):
    session.add(client)
    session.commit()


def update_client(client: Client):
    old_client: Client = session.query(Client).where(id_client=client.id_client).first()
    old_client.nom = client.nom
    old_client.prenom = client.prenom
    old_client.gsm = client.gsm
    session.add(old_client)
    session.commit()


def delete_client(client: Client):
    session.delete(client)
    session.commit()


def get_all_client() -> list[Client]:
    return session.query(Client).all()


def get_client_by_id(id_client: int) -> Client:
    return session.query(Client).where(id_client=id_client).first()
