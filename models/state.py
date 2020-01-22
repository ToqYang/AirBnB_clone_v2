#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'

    @property
    def cities(self):
        """
        returns City's with same State.id
        """
        mydict = models.storage.all(City)
        cities = []

        for states, city in mydict.items():
            if city.state_id == self.id:
                cities.append(city)
        return cities
