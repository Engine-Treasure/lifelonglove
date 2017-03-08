# -*- coding:utf-8 -*-

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)  # Flask 用这个参数决策程序根目录, 以方便地对资源进行定位

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
