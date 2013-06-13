# -*- coding:utf-8 -*-
from sheep.api.cache import cache, backend

from models import db, IntegrityError
from models.base import BaseLikeObject
from models.consts import LIKE, DISLIKE 

_LIKE_NUM_TARGET = 'like:target:%s:%s'
_DISLIKE_NUM_TARGET = 'hate:target:%s:%s'

class LikeItem(db.Model, BaseLikeObject):
    __tablename__ = 'like'
    __table_args__ = (db.UniqueConstraint('user', 'target', 'kind',
        name='uk_user_target_kind'),)
    
    def __init__(self, user, target, action, time, kind):
        self.user = user
        self.target = target
        self.action = action
        self.kind = kind

    @classmethod
    def add_like(cls, user_id, target, kind):
        try:
            like = cls(user_id, target, LIKE, kind)
            db.session.add(like)
            db.session.commit()
            _flush_like_num(target, kind)
        except IntegrityError:
            db.session.rollback()
            db.session.query(cls).filter_by(user=user_id, target=target, kind=kind).\
                    update({action: LIKE})
            db.session.commit()
        return like

    @classmethod
    def add_dislike(cls, user, target, kind):
        try:
            like = cls(user, target, DISLIKE, kind)
            db.session.add(like)
            db.session.commit()
            _flush_dislike_num(target, kind)
        except IntegrityError:
            db.session.query(cls).filter_by(user=user_id, target=target, kind=kind).\
                    update({action: DISLIKE})
            db.session.commit()
        return like

    @classmethod
    @cache(_LIKE_NUM_TARGET % ('{target}', '{kind}'))
    def get_like_num_by_target(cls, target, kind):
        db.session.query(cls.id).filter_by(kind=kind, target=target,
                action=LIKE).count()

    @classmethod
    @cache(_DISLIKE_NUM_TARGET % ('{target}', '{kind}'))
    def get_dislike_num_by_target(cls, target, kind):
        db.session.query(cls.id).filter_by(kind=kind, target=target,
                action=DISLIKE).count()

def _flush_like_num(target, kind):
    backend.delete(_LIKE_NUM_TARGET % (target, kind))

def _flush_dislike_num(target, kind):
    backend.delete(_DISLIKE_NUM_TARGET % (target, kind))

