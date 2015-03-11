# coding=utf-8
from blog.handlers.home import HomeHandler
from blog.handlers.post import PostHandler


urls = [
    (r"/", HomeHandler, None, 'home'),
    (r"/page/(\d+)", HomeHandler, None, 'home_paged'),
    (r"/posts/(.+)", PostHandler, None, 'post'),
]