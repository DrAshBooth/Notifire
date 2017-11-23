from pymongo import MongoClient
from werkzeug.security import generate_password_hash


mongo_client = MongoClient("mongodb:27017")
notifire_db = mongo_client.notifire_db


def create_users():
    return [
        {
            "Username": "ash",
            "Password": generate_password_hash("password")
        },
        {
            "Username": "john",
            "Password": generate_password_hash("password")
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
