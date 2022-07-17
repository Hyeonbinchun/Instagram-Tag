from email.mime import base
from flask import Blueprint, request
from app import client
import datetime
from base64 import b64encode
import requests
import json
from dotenv import load_dotenv
import os
import cloudinary
# import cloudinary.uploader
from cloudinary import uploader
from bson.objectid import ObjectId

load_dotenv()

project = Blueprint("user", __name__)  # initialize blueprint
db = client.pizza

cloudinary.config(
    cloud_name="dz03b1a69",
    api_key= os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)


# function that is called when you visit /
@project.route("/api/tags", methods=["POST"])
def get_tags():
    # Receive an image
    imagefile = request.files.get('img', '')
    file_to_upload = request.files.get("file", '')
    # imagefile = file_to_upload
    # Convert image to base64
    base64_img = b64encode(imagefile.read())

    # Pass image base64 data to Google Vision API (refer to postman)

    url = "https://vision.googleapis.com/v1/images:annotate?key=" + \
        os.getenv('GOOGLE_API')


    payload = json.dumps({
        "requests": [
            {
                "image": {"content": base64_img.decode()},
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 5
                    }
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    res = json.loads(response.text)

    lst = []
    for i in range(len(res["responses"][0]["labelAnnotations"])):
        lst.append(res["responses"][0]["labelAnnotations"][i]["description"])

    # Parse out tags from Google Vision API Data

    # Return list of tags as JSON
    """
    {
        tags: ["clouds", "nature"],
        msg: "success"
    }
    """
    # file_to_upload = 'data:image/png;base64,{}'.format(base64_img[2:])
    # print(base64_img[:30])
    # print(file_to_upload[:30])
    res = cloudinary.uploader.upload(file_to_upload)

    #1. Get img link from res
    image_link = res['url']
    print(image_link)

    #2. insert image link and tags into mongodb (to do this, you need to setup mongodb client inside this file)
    user_data = {"tags": lst, "image_link": image_link}
    db.images.insert_one(user_data)
    return {
        "msg": "success"
    }


@project.route("/api/images", methods=["GET"])
def get_all_image():
    image = list(db.images.find({}))
    return {
        "msg": "Success",
        "data": image
    }

@project.route("/api/tags", methods=["GET"])
def get_image():
    user_data = request.get_json()
    objInstance = ObjectId(user_data['_id'])
    image = db.images.find_one(objInstance)
    return {
        "msg": "Success",
        "data": image
    }

@project.route("/api/tags", methods=["DELETE"])
def delete_image():
    # delete by searching for username
    user_data = request.get_json()
    print(user_data)
    objInstance = ObjectId(user_data['_id'])
    objInstance2 = {"_id": objInstance}
    db.images.delete_one(objInstance2)
    return {
        "msg": "Successfully deleted",
    }

@project.route("/api/tags/custom", methods=["PUT"])
def add_custom_tag():

    # 1. Get id and custom tags from json
    user_data = request.get_json()
    print(user_data)

    # 3. Append new custom tag to the list
    db.images.update_one({'_id': ObjectId(user_data['_id'])}, {'$push': {'tags': user_data['tag']}})
    # 4. Using update_one, update document with given id and update new tags with new list

    return {
        "msg": "Successfully added"
    }

@project.route("/api/tags/custom", methods=["DELETE"])
def delete_custom_tag():

    # 1. Get id and custom tags from json
    user_data = request.get_json()
    objInstance = ObjectId(user_data['_id'])
    image = db.images.find_one(objInstance)
    tags = image["tags"]
    # 3. Delete tag in the list
    if user_data["tag"] in tags:
        tags.remove(user_data["tag"])
    # 4. Using update_one, update document with given id and update new tags with new list
    
    user_data = request.get_json()
    new = {"$set":{}}
    new["$set"]["tags"] = tags
    db.images.update_one({'_id': ObjectId(user_data['_id'])}, new)

    return {
        "msg": "Successfully deleted"
    }