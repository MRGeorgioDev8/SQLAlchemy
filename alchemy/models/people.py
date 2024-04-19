from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)

    special_id = Column(Integer, ForeignKey('special.id'), name='profession')
    special = relationship('Special', back_populates='people', primaryjoin='People.special_id == Special.id')

    def __init__(self, full_name, age, special_id):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.special_id = special_id

    def __repr__(self):
        return f"{self.id} {self.surname} {self.name} {self.patronymic} возраст:{self.age}"