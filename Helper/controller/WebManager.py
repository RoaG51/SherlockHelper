# -*- coding: utf-8 -*-
from Helper import app
from flask import render_template
from innerFunctions import refreshProSpace


@app.route('/')
def show_index():
    refreshProSpace(9,10,11,12)
    return render_template('index.html')

