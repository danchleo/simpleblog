# coding=utf-8
import sys
import tornado.ioloop
import tornado.web
import blog.settings
import blog.monitor

__import__(blog.settings.URL)
_url_module = sys.modules[blog.settings.URL]
application = tornado.web.Application(_url_module.urls)


if __name__ == "__main__":
    ioloop = tornado.ioloop.IOLoop.instance()
    notifier = blog.monitor.Monitor(blog.settings.POST_DIR, ioloop)
    application.listen(8888)
    
    try:
        ioloop.start()
    except KeyboardInterrupt:
        ioloop.close()
        notifier.stop()
