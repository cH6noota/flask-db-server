# coding: utf-8
from flask import Flask
from flask_restful import Api
from database import init_db
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config.Config')

# DB init
init_db(app)
api = Api(app)
ma = Marshmallow(app)

from lib.create_init import create_init
create_init(app)

from models.user import Userapi
api.add_resource(Userapi, '/user')


if __name__ == "__main__":
    app.run(debug=False)