import datetime
from pymongo import MongoClient


mongo_client = MongoClient("mongodb:27017")
notifire_db = mongo_client.notifire_db


def create_users():
    return [
        {
            "First Name": "Ash",
            "Last Name": "Booth",
            "Username": "43857264",
            "Password": "password",
            "DateCreated": datetime.datetime.now()
        },
        {
            "First Name": "John",
            "Last Name": "Doe",
            "Username": "43857250",
            "Password": "password",
            "DateCreated": datetime.datetime.now()
        }

    ]


def drop_db():
    notifire_db.Users.drop()


def build_db():
    user_collection = notifire_db.Users
    user_collection.insert_many(create_users())


if __name__ == "__main__":
    print("started DB initialization")
    drop_db()
    build_db()
    print("finished DB initialization")
