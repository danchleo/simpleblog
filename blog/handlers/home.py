# coding=utf-8
import tornado.web


class HomeHandler(tornado.web.RequestHandler):
    def get(self, page=1):
        self.write('page:%s' % page)