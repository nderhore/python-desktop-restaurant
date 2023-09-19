from sqlalchemy import Column, Integer, String

from config.database import Base


class Client(Base):
    __tablename__ = "client"
    id_client = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    gsm = Column(String(10), nullable=False)
