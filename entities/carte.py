from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base
from entities.restaurant import Restaurant


class Carte(Base):
    __tablename__ = "carte"
    id = Column(Integer, primary_key=True, autoincrement=True)
    carte_gastronomique = Column(Boolean, nullable=False)
    id_restaurant = Column(
        Integer, ForeignKey("restaurant.id_restaurant"), nullable=False
    )
    restaurant = relationship(Restaurant)
