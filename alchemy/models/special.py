from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base

class Special(Base):
    __tablename__ = 'special'

    id = Column(Integer, primary_key=True)
    special_title = Column(String(250), nullable=False)
    people = relationship('People', back_populates='special')

    def __repr__(self):
        return f"{self.id} {self.special_title}"