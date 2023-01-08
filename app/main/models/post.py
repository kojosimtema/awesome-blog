from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.main.db import Base
from datetime import datetime

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer(), primary_key=True)
    title = Column(String(20), nullable=False)
    content = Column(String(800), nullable=False)
    image = Column(String(), default='default_post_photo.jpg')
    username = Column(String(), ForeignKey('users.username'), nullable=False)
    no_of_views = Column(Integer(), default=0)
    date_added = Column(DateTime(), default=datetime.utcnow)
    date_updated = Column(DateTime(), default=datetime.utcnow)    
    
    
    def __repr__(self):
        return f'<Title {self.title}>'