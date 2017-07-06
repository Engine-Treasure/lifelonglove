# -*- coding: utf-8 -*-

from __future__ import absolute_import


from flask import render_template

from . import blessing

__author__ = "kissg"
__date__ = "2017-05-09"


@blessing.route("/", methods=["GET"])
def index():
    return render_template("blessing/index.html")