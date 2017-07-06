# -*- coding: utf-8 -*-


import os


__author__ = "kissg"
__date__ = "2017-05-08"


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 通用密钥, 可在 Flask 和多个第三方扩展中使用.
    # 本项目中, 用于为 Flask-WTF 生成加密密令
    SECRET_KEY = os.environ.get("SECRET_KEY") \
                 or "Engine, will you love Echo forever?"

    BLESSING_MAIL_SUBJECT_PREFIX = "【All The Blessings】"
    BLESSING_MAIL_SENDER = "All the Blessings <blessing@kissg.org>"
    ADMIN = os.environ.get("BLESSING_ADMIN")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


config = {
    "development": DevelopmentConfig,

    "default": DevelopmentConfig
}
