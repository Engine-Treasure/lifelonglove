# -*- coding: utf-8 -*-

from flask import Blueprint

__author__ = "kissg"
__date__ = "2017-05-09"

blessing = Blueprint("blessing", __name__)

from . import views