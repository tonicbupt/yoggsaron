# -*- coding:utf-8 -*-
from models import db
from models.base import BaseObject
from models.mixin.comment import CommentMixin

class Restaurant(db.Model, BaseObject, CommentMixin):
    addr = db.Column('addr', db.String(255), nullable=False)
    poi = db.Column('poi', db.String(255), nullable=True)
    __tablename__ = 'restaurant'
    _CACHE_KEY = 'rest:%s'
    type = 'restaurant'

    def __init__(self, name, desc, tags, kind, addr, poi, pic):
        self.name = name
        self.desc = desc
        self.tags = tags
        self.kind = kind
        self.addr = addr
        self.poi = poi
        self.pic = pic
        
