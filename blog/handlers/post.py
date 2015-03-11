# coding=utf-8
import tornado.web
from blog.models import PostModel, RecordNotFound


class PostHandler(tornado.web.RequestHandler):
    def get(self, key):
        try:
            post = PostModel.get(key)
        except RecordNotFound:
            raise tornado.web.HTTPError(404)
            
        print post.title
        print repr(post.created_at)
        print repr(post.content)
        print post.html
        
        self.write('md key:%s' % key)