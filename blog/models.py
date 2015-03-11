# coding=utf-8
import os
import datetime
import blog.settings
from blog.model_render import PostRender


class RecordNotFound(Exception):
    pass


class BaseModel(object):
    def __init__(self, **kwargs):
        super(BaseModel, self).__init__()
        for k in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[k])
                
    @classmethod
    def get(cls, key):
        _dir = blog.settings.POST_DIR
        filename = os.path.join(_dir, '%s.md' % key)
        filename = os.path.abspath(filename)
        if not filename.startswith(_dir) or not os.path.exists(filename):
            raise RecordNotFound()
        
        o = cls()
        _start = False
        
        with open(filename, 'rb') as h:
            while True:
                line = h.readline()
                if not line:
                    break
                
                line = line.strip()
                if not line:
                    _start = True
                    o.content = ''
                    continue
                
                if _start:
                    o.content += line
                    o.content += '\n'
                    
                else:
                    attr_name, _t, value = line.partition(':')
                    setattr(o, attr_name, value.strip())
        
        o.html = PostRender.parse(o.content)
        return o
    
    @classmethod
    def all(cls, **kwargs):
        pass
    

class PostModel(BaseModel):
    title = None
    tag = []
    category = None
    author = None
    _created_at = None
    _modified_at = None
    content = None
    html = None
    
    @property
    def created_at(self):
        return self._created_at
        
    @created_at.setter
    def created_at(self, value):
        if isinstance(value, datetime.datetime):
            self._created_at = value
            
        elif isinstance(value, str):
            try:
                self._created_at = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                pass
    
    @property
    def modified_at(self):
        return self._modified_at
        
    @modified_at.setter
    def modified_at(self, value):
        if isinstance(value, datetime.datetime):
            self._modified_at = value
            
        elif isinstance(value, str):
            try:
                self._modified_at = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                pass
    
            
            
            
        
        