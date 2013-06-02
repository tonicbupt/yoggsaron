# -*- coding:utf-8 -*-

from sheep.api.service import get_service
from utils import service_exception

COMMENT_SERVICE_NAME = 'service.api'

# TODO unix = ?
comment_service = get_service(COMMENT_SERVICE_NAME, unix='')

class CommentMixin(object):
    comment_type = ''

    @service_exception
    def add_comment(self, author, text, ref_id=0, privacy=0):
        return comment_service.add_comment(self.comment_type, self.id, author,
                text, ref_id=ref_id, privacy=privacy)

    @service_exception
    def remove_comment(self, author, cid):
        return comment_service.del_comment(author, cid)

    @service_exception
    def get_comments(self, start, limit):
        return comment_service.get_comments(self.comment_type, self.id, start, limit)
