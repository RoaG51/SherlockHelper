# -*- coding: utf-8 -*-
from Helper import app
from Helper.model.s_data_prospace import s_data_prospace
from flask import render_template
from innerFunctions import initGameData,showMurderer,setPlayerChara


@app.route('/')
def show_index():
    initGameData((9,10,11,12))
    myChara = setPlayerChara((9,10,11,12))
    myResults = showMurderer()
    myGameDatas = s_data_prospace.query.all()
    curNum = s_data_prospace.query.count()
    return render_template('index.html',myChara = myChara, results = myResults,gameDatas = myGameDatas[0:10],curNum = curNum)

