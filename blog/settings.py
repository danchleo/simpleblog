# coding=utf-8
import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

URL = 'blog.urls'

DATA_DIR = os.path.join(BASE_DIR, 'data')

POST_DIR = os.path.join(DATA_DIR, 'posts')