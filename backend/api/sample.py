from flask import Blueprint, request
from app import client

sample = Blueprint("sample", __name__)  # initialize blueprint
db = client.pizza

# function that is called when you visit /
@sample.route("/")
def index():
    print("hit")
    return {
        "data": db.list_collection_names()
    }


@sample.route("/api/health-check")
def health_check():
    return "Success."

@sample.route("/api/hyeonbin")
def return_dictionary():
    return {"Name":"Hyeonbin", "Age":21, "University": "University of Toronto"} 
