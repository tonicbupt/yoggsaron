# -*- coding:utf-8 -*-
from sheep.api.cache import cache, backend

from models import db
from models.base import BaseObject

_FOOD_KEY = 'food:%s'

class Food(db.Model, BaseObject):
    price = db.Column('price', db.Integer, nullable=True)
    __tablename__ = 'food'
    type = 'food'

    def __init__(self, name, desc, tags, kind, price, pic):
        self.name = name
        self.desc = desc
        self.tags = tags
        self.kind = kind
        self.price = price
        self.pic = pic

    @classmethod
    @cache(_FOOD_KEY % '{id}')
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def gets(cls, ids):
        return [cls.get(i) for i in ids]

def _flush_food(id):
    backend.delete(_FOOD_KEY % id)

