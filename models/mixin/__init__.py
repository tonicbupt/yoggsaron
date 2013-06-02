# -*- coding:utf-8 -*-
from sheep.api.cache import cache, backend

class BaseObjectMixin(object):
    _CACHE_KEY = '%s'
    
    @classmethod
    @cache(_CACHE_KEY % '{id}')
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def gets(cls, ids):
        return [cls.get(i) for i in ids]

    def _flush_cache(self):
        backend.delete(_CACHE_KEY % self.id)

