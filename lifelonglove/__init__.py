# -*- coding:utf-8 -*-

from __future__ import absolute_import

from flask import Flask
from flask_bootstrap import Bootstrap

from config import config

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)  # Flask 用这个参数决策程序根目录, 以方便地对资源进行定位
    app.debug = True

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册回调函数, 实现各功能
    bootstrap.init_app(app)

    from .blessing import blessing as bp_blessing
    app.register_blueprint(bp_blessing, url_prefix="/blessing")

    from .moment import moment as bp_moment
    app.register_blueprint(bp_moment, url_prefix="/moment")

    return app
