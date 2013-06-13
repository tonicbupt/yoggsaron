# -*- coding:utf-8 -*-
from datetime import datetime
from models import db

class BaseObject(object):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False, index=True)
    desc = db.Column('desc', db.Text, nullable=True)
    time = db.Column('time', db.DateTime, default=datetime.now)
    tags = db.Column('tags', db.String(255), nullable=True)
    kind = db.Column('kind', db.String(255), nullable=True, index=True)
    pic = db.Column('pic', db.String(255), nullable=True)
    like = db.Column('like', db.Integer, default=0, index=True)
    dislike = db.Column('dislike', db.Integer, default=0, index=True)

class BaseTopic(object):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    author = db.Column('author', db.Integer, nullable=False, index=True)
    text = db.Column('text', db.Text, nullable=False)
    time = db.Column('time', db.DateTime, default=datetime.now)
    tags = db.Column('tags', db.String(255), nullable=True)
    like = db.Column('like', db.Integer, default=0, index=True)
    dislike = db.Column('dislike', db.Integer, default=0, index=True)

class BaseLikeObject(object):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    target = db.Column('target', db.Integer, nullable=False, index=True)
    user = db.Column('user', db.Integer, nullable=False, index=True)
    action = db.Column('action', db.CHAR, nullable=False, index=True)
    kind = db.Column('kind', db.Integer, default=0, index=True)
