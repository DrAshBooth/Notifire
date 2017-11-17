from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from redis import Redis, RedisError

import config
import socket

# Connect to Redis
redis = Redis(host="redis", port=6379)


class HelloHandler(RequestHandler):
    def get(self):
        try:
            visits = redis.incr("counter")
        except RedisError:
            visits = "could not connect to Redis"

        html = "<h3>Hello {name}!</h3>" \
               "<b>Hostname:</b> {hostname}<br/>" \
               "<b>Visits:</b> {visits}"
        self.write(html.format(name="world",
                               hostname=socket.gethostname(),
                               visits=visits))


class IndexPageHandler(RequestHandler):
    def get(self):
        self.render("index.html")


class MyWsHandler(WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        self.write_message(u"Your message was: " + message)

    def on_close(self):
        pass


def make_app():
    handlers = [
        (r'/hello', HelloHandler),
        (r'/', IndexPageHandler),
        (r'/websocket', MyWsHandler)
    ]
    settings = {
        'template_path': config.TEMPLATE_PATH
    }
    return Application(
        handlers,
        **settings
    )

if __name__ == "__main__":
    app = make_app()
    server = HTTPServer(app)
    server.listen(80)
    IOLoop.instance().start()
