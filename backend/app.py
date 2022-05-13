import json
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
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

client = MongoClient('localhost', 27017, username='username', password='password')

def create_app():
    """ Creates and initializes a Flask object to be used
    """

    app = Flask(__name__)
    # configure_mongo_uri(app)
    CORS(app, supports_credentials=True)
    app.json_encoder = JSONEncoder
    register_blueprints(app)

    return app



def register_blueprints(app):
    """ Helper function to register all the controllers/API into Flask app object
    """

    from api.sample import sample


    print("Registering blueprints into app.")

    app.register_blueprint(sample)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()