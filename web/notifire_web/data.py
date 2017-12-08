from pymongo import MongoClient
from werkzeug.security import check_password_hash


class User(object):
    def __init__(self, doc):
        self.pw_hash = doc["Password"]
        self.username = doc["Username"]

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.pw_hash, password)


class DataService(object):
    def __init__(self):
        mongo_client = MongoClient("mongodb:27017")
        self._notifire_db = mongo_client.notifire_db

    def get_user(self, username: str) -> User:
        user_doc = self._notifire_db.Users.find_one({"Username": username})
        if user_doc is not None:
            return User(user_doc)

    def get_users(self):
        users = self._notifire_db.Users.find()
        return [user for user in users]
