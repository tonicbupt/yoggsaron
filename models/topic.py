# -*- coding:utf-8 -*-
from models import db
from models.base import BaseTopic
from models.mixin.comment import CommentMixin

class Topic(db.Model, BaseTopic, CommentMixin):
    __tablename__ = 'topic'
    _CACHE_KEY = 'topic:%s'
    type = 'topic'

    def __init__(self, author, text, tags):
        self.author = author
        self.text = text
        self.tags = tags

    @classmethod
    def create(cls, author, text, tags):
        t = cls(author, text, tags)
        db.session.add(t)
        db.session.commit()
        return t

    def delete(self, user_id):
        if user_id != self.author:
            return
        db.session.delete(self)
        db.session.commit()
        self._flush_cache()

