from sqlalchemy import Column, Integer, String, DateTime
from flask_login import UserMixin
from app.main.db import Base


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    display_pic = Column(String(), default='default_photo.jpg')
    background_pic = Column(String(), default='blue_background.jpg')
    username = Column(String(10), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(500))
    

    def __repr__(self):
        return f'<User {self.first_name}>'

    