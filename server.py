#!/usr/bin/env python
import locale

from tornado.options import options, define, parse_command_line
import django
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os

define('port', type=int, default=int(os.environ.get('SERVER_PORT', 8000)))
define('address', type=str, default=os.environ.get('SERVER_HOST', "0.0.0.0"))


class HelloTornadoHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write('Hello from tornado')


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "md.settings")

    locale.setlocale(locale.LC_TIME, locale.getdefaultlocale())
    tornado.options.parse_command_line()

    django.setup()
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())

    tornado_app = tornado.web.Application(
        [
            ('/hello-tornado', HelloTornadoHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ])

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port, address=options.address)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
