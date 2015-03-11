# coding=utf-8
import os
import time
import tornado.ioloop
from pyinotify import WatchManager
from pyinotify import IN_DELETE, IN_CREATE, IN_MODIFY
from pyinotify import TornadoAsyncNotifier


class AsyncNotifier(TornadoAsyncNotifier):
    def __init__(self, wm, ioloop, *args, **kwargs):
        kwargs['default_proc_fun'] = self.process_event
        TornadoAsyncNotifier.__init__(self, wm, ioloop, *args, **kwargs)
        self.periodic = tornado.ioloop.PeriodicCallback(self.refresh, 30000, ioloop)
        
    def _is_md(self, filename):
        if os.path.splitext(filename)[1] == ".md":
            return True
        return False
        
    def process_event(self, event):
        filename = os.path.join(event.path, event.name)
        if self._is_md(filename):
            if self.periodic._running:
                self.periodic.stop()
            print 'scheduled: %s' % time.time()
            self.periodic.start()

    def refresh(self):
        print 'refreshing: %s' % time.time()
        self.periodic.stop()


def Monitor(path, ioloop):
    wm = WatchManager()
    wm.add_watch(path, IN_CREATE | IN_MODIFY | IN_DELETE)
    return AsyncNotifier(wm, ioloop)
