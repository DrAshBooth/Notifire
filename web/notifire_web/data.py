
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    def __init__(self, username, password):
        self.pw_hash = generate_password_hash(password)
        self.username = username

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class DataService(object):
    def __init__(self):
        mongo_client = MongoClient("mongodb:27017")
        self._notifire_db = mongo_client.notifire_db

    def get_users(self):
        users = self._notifire_db.Users.find()
        return [user for user in users]