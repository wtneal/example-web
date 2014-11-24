from flask import Flask
from flask.ext import restful
from flask.ext.script import Manager

app = Flask(__name__)
app.config.from_object('config')

api = restful.Api(app)

manager = Manager(app)

import routes
