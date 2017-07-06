# -*- coding: utf-8 -*-

from __future__ import absolute_import


from flask import render_template

from . import moment

__author__ = "kissg"
__date__ = "2017-05-09"


@moment.route("/", methods=["GET"])
def index():
    return render_template("moment/index.html")
