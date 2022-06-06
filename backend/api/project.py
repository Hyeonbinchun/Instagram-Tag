from flask import Blueprint, request
from app import client
import datetime
from base64 import b64encode
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

project = Blueprint("user", __name__)  # initialize blueprint
db = client.pizza


# function that is called when you visit /
@project.route("/api/tags", methods=["POST"])
def get_tags():
    # Receive an image
    imagefile = request.files.get('img', '')

    # Convert image to base64
    base64_img = b64encode(imagefile.read())
    print(str(base64_img)[0:10])

    # Pass image base64 data to Google Vision API (refer to postman)

    url = "https://vision.googleapis.com/v1/images:annotate?key=" + os.getenv('GOOGLE_API')

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

    return {"tags": lst, "msg": "success"}
