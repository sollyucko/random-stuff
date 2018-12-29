from easy_wsgi.typing import Environ, StartResponse, WSGIApp


class DBObject: pass


class App(WSGIApp):
    def __init__(self, environ: Environ, start_response: StartResponse):
        cls = self.__class__
        
        for obj in cls.__dict__.values():
            if isinstance(obj, type):
                if issubclass(obj, DBObject):
                    pass
