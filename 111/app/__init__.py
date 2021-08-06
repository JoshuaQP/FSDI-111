#!/usr/bin/env python3
# -*- coding: utf8 -*-
# "simple flask app"


from flask import Flask

app = Flask(__name__)


@app.route("/aboutme")
def about_me():
    me ={

      "first_name":"joshua",
      "first_name":"joshua",
      "first_name":"joshua",
      "first_name":"joshua",
      "test": True


    }

    return me

    