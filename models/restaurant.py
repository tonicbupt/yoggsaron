# -*- coding:utf-8 -*-
from sheep.api.cache import cache, backend

from models import db
from models.base import BaseObject
from models.mixin.comment import CommentMixin

_RESTAURANT_KEY = 'rest:%s'

class Restaurant(db.Model, BaseObject, CommentMixin):
    addr = db.Column('addr', db.String(255), nullable=False)
    poi = db.Column('poi', db.String(255), nullable=True)
    __tablename__ = 'restaurant'
    type = 'restaurant'

    def __init__(self, name, desc, tags, kind, addr, poi, pic):
        self.name = name
        self.desc = desc
        self.tags = tags
        self.kind = kind
        self.addr = addr
        self.poi = poi
        self.pic = pic
        
    @classmethod
    @cache(_RESTAURANT_KEY % '{id}')
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def gets(cls, ids):
        return [cls.get(i) for i in ids]

def _flush_restaurant(id):
    backend.delete(_RESTAURANT_KEY % id)
