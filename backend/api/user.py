from flask import Blueprint, request
from app import client
import datetime

user = Blueprint("user", __name__)  # initialize blueprint
db = client.pizza

"""
This is for practice
"""

# function that is called when you visit /
@user.route("/api/user/create", methods=["POST"])
def create_user():
    user_data = request.get_json()
    db.user.insert_one(user_data)
    return {
        "dmsg": "success"
    }


@user.route("/api/user/read", methods = ["GET"])
def read_user():
    user_data = request.get_json()
    user = db.user.find_one(user_data)
    return {
        "msg": "Success",
        "data": user
    }

@user.route("/api/user/update", methods = ["PUT"])
def update_user():
    # update by seraching for username
    user_data = request.get_json()
    # new = {"$set": {"user": "Hyeonbin"}}
    new = {"$set":{}}
    if "name" in user_data:
        new["$set"]["name"] = user_data["name"]
    if "password" in user_data:
        new["$set"]["password"] = user_data["password"]
    db.user.update_one({
        "user":user_data["user"]
        }, 
        new)

    return {
        "msg": "Successfully updated",
    }


@user.route("/api/user/delete", methods = ["DELETE"])
def delete_user():
    # delete by searching for username
    user_data = request.get_json()
    db.user.delete_one(user_data)
    return {
        "msg": "Successfully deleted",
    }
