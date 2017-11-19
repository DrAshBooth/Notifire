
from pymongo import MongoClient


class DataService(object):
    def __init__(self):
        mongo_client = MongoClient("mongodb:27017")
        self._notifire_db = mongo_client.notifire_db

    def get_users(self):
        users = self._notifire_db.Users.find()
        return [user for user in users]