import json
from flask import Flask
from flask_cors import CORS
import pymongo
import certifi
# from pymongo import MongoClient
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    """ extend json-encoder class 
    """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

# client = MongoClient('localhost', 27017, username='username', password='password')
client = pymongo.MongoClient("mongodb+srv://admin:password123!@cluster0.s2yij.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())

def create_app():
    """ Creates and initializes a Flask object to be used
    """

    app = Flask(__name__)
    # configure_mongo_uri(app)
    print('Connecting DB')
    CORS(app, supports_credentials=True)
    app.json_encoder = JSONEncoder
    register_blueprints(app)

    return app



def register_blueprints(app):
    """ Helper function to register all the controllers/API into Flask app object
    """

    from api.sample import sample
    from api.user import user


    print("Registering blueprints into app.")

    app.register_blueprint(sample)
    app.register_blueprint(user)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')