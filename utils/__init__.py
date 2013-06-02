# -*- coding:utf-8 -*-
from functools import wraps

def service_exception(f):
    @wraps(f)
    def _(*a, **kw):
        try:
            c = f(*a, **kw)
        except Exception, e:
            c = {}
        return c
    return _
