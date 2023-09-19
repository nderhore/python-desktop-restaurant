from sqlalchemy import Column, Integer, String

from config.database import Base


class Restaurant(Base):
    __tablename__ = "restaurant"
    id_restaurant = Column(Integer, primary_key=True, autoincrement=True)
    capacite_max_midi = Column(Integer, nullable=False)
    capacite_max_soir = Column(Integer, nullable=False)
    horaire_midi = Column(String(50), nullable=False)
    horaire_soir = Column(String(50), nullable=False)
