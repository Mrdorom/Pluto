"""
-------------------------------------------------
File Name：   run
Description :
Author :       shili
date：          2021/3/11
-------------------------------------------------
Change Activity: 2021/3/11:
-------------------------------------------------
"""
__author__ = 'shili'

from flask import Flask
from config import DefaultConfig
from apps.extend import mongo,jwt
from apps import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)
    jwt.init_app(app)
    mongo.init_app(app)
    return app


app = create_app()
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(threaded=True)

