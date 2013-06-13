# -*- coding:utf-8 -*-
from sheep.api.cache import cache, backend

from models import db
from models.base import BaseTopic
from models.like import LikeItem
from models.mixin.comment import CommentMixin
from models.consts import KIND_TOPIC

_TOPIC_KEY = 'topic:%s'

class Topic(db.Model, BaseTopic, CommentMixin):
    __tablename__ = 'topic'
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

    @classmethod
    @cache(_TOPIC_KEY % '{id}')
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def gets(cls, ids):
        return [cls.get(i) for i in ids]

    def delete(self, user_id):
        if user_id != self.author:
            return
        db.session.delete(self)
        db.session.commit()
        _flush_topic(self.id)

    def add_like(self, user_id):
        LikeItem.add_like(user_id, self.id, KIND_TOPIC)
        self.like += 1
        db.session.add(self)
        db.session.commit()
        _flush_topic(self.id)

    def add_dislike(self, user_id):
        LikeItem.add_dislike(user_id, self.id, KIND_TOPIC)
        self.dislike += 1
        db.session.add(self)
        db.session.commit()
        _flush_topic(self.id)

def _flush_topic(id):
    backend.delete(_TOPIC_KEY % id)
