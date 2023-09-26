from sqlalchemy import Integer, Column, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base
from entities.categorie import Categorie


class Plat(Base):
    __tablename__ = "plat"
    id_plat = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    allergene = Column(String(50), nullable=False)
    prix = Column(Float, nullable=False)
    archive = Column(Boolean, nullable=False)
    id_categorie = Column(Integer, ForeignKey("categorie.id_categorie"), nullable=False)
    categorie = relationship(Categorie)
