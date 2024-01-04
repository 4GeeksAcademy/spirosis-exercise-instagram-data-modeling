import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), unique = True, nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), unique = True, nullable=False)
    phone = Column(String(250), unique = True, nullable=False)
    bio = Column(String(500), nullable=False)
    url = Column(String(300), unique = True, nullable=False)
    website = Column(String(250), unique = True, nullable=False)
    photoId = Column(Integer, nullable = True)

class Login(Base):
    __tablename__ = 'login'

    id = Column(Integer, primary_key = True)
    username = Column(String(250), ForeignKey('user.username'))
    password = Column(String(250), ForeignKey('user.password'))

    login = relationship('User')
   
class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key = True)
    description = Column(String(250), nullable = True)
    location = Column(String(250), nullable = True)
    tags = Column(String(50), nullable = True)
    postId = Column(Integer, ForeignKey('post.id'))
    likes = Column(Integer, nullable = False)
    userId = Column(Integer, ForeignKey('user.id'))

    photo = relationship('User')

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    avatarURL = Column(String(250), nullable = False)
    comment = Column(String(250), nullable = False)
    userId = Column(Integer, ForeignKey('user.id'))
    username = Column(String(250), ForeignKey('user.username'))

    comments = relationship('Photo')

class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    avatarURL = Column(String(250), nullable = False)
    username = Column(String(250), ForeignKey('user.username'))

    like = relationship('Photo')

class Notifications(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    temps = Column(String(250), nullable = False)
    userId = Column(Integer, ForeignKey('user.id'))

class Followers(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique = True)
    followerId = Column(Integer, unique = True)
    userId = Column(Integer, ForeignKey('user.id'))

    user_followers = relationship('User')
    notifications_followers = relationship('Notifications')

class Profile(Base):
    __tablename__ = 'profile'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable = False)
    userId = Column(Integer, ForeignKey('user.id'))
    photoId = Column(Integer, ForeignKey('user.photoId'))

    profile_photo = relationship('Photo')
    profile_user = relationship('User')

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    caption = Column(Text, nullable = True)
    imageURL = Column(String)
    userId = Column(Integer, ForeignKey('user.id'))

    user_post = relationship('User')
    profile_post = relationship('Profile')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
