# -*- coding:utf-8 -*-
from models import db
from models.base import BaseObject

class Food(db.Model, BaseObject):
    price = db.Column('price', db.Integer, nullable=True)
    __tablename__ = 'food'
    _CACHE_KEY = 'food:%s'
    type = 'food'

    def __init__(self, name, desc, tags, kind, price, pic):
        self.name = name
        self.desc = desc
        self.tags = tags
        self.kind = kind
        self.price = price
        self.pic = pic
