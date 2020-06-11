from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS








app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ag.db'
app.config['CLIENT_IMAGES']= '/Users/useradmin1/PycharmProjects/agapi/agapi/static/posts/'
db = SQLAlchemy(app)
ma = Marshmallow(app)
from agapi import routes

CORS(app)

