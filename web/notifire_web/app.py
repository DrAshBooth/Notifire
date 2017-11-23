import socket
import sys
import os

from redis import Redis, RedisError
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, authenticated
from tornado.websocket import WebSocketHandler
# from tornado.escape import xhtml_escape

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from notifire_web.config import TEMPLATE_PATH
from notifire_web.data import DataService


# Connect to Redis
redis = Redis(host="redis", port=6379)

# Conect to MongoDB - via service
ds = DataService()


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


# class AuthLoginHandler(BaseHandler):
#     def get(self):
#         try:
#             errormessage = self.get_argument("error")
#         except:
#             errormessage = ""
#         self.render("login.html", errormessage = errormessage)
#
#     def check_permission(self, username, password):
#         if username == "admin" and password == "admin":
#             return True
#         return False


class HelloHandler(RequestHandler):
    # @authenticated
    def get(self):
        try:
            visits = redis.incr("counter")
        except RedisError:
            visits = "could not connect to Redis"

        html = "<h3>Hello {name}!</h3>" \
               "<b>Hostname:</b> {hostname}<br/>" \
               "<b>Visits:</b> {visits}"

        # user = xhtml_escape(self.current_user)

        self.write(html.format(name="World",
                               hostname=socket.gethostname(),
                               visits=visits))


class UserHandler(RequestHandler):
    def get(self):
        _users = ds.get_users()
        users = [str(u) for u in _users]
        self.render("users.html", users=users)


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
        # (r"/auth/login/", AuthLoginHandler),
        (r'/websocket', MyWsHandler),
        (r'/users', UserHandler)
    ]
    settings = {
        'template_path': TEMPLATE_PATH,
        # "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        # "login_url": "/auth/login/"
    }
    return Application(
        handlers,
        **settings
    )


if __name__ == "__main__":
    app = make_app()
    server = HTTPServer(app)
    server.listen(5050)
    IOLoop.instance().start()
