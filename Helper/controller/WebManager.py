# -*- coding: utf-8 -*-
from Helper import app
from Helper.model.s_data_prospace import s_data_prospace
from flask import render_template,request,session,url_for,redirect
from innerFunctions import initGameData,showMurderer,setPlayerChara,listStringtoInt,deleteGameData,delDB


@app.route('/')
def show_index():
    if session.has_key('myRoles'):
        myChara = setPlayerChara(session["myRoles"])
    else:
        myChara = setPlayerChara()
    myResults = showMurderer()
    myGameDatas = s_data_prospace.query.order_by(s_data_prospace.C).all()
    curNum = s_data_prospace.query.count()
    return render_template('index.html',myChara = myChara, results = myResults,gameDatas = myGameDatas[0:10],curNum = curNum)

@app.route('/Init',methods=["POST"])
def initMyRoles():
    if request.method == "POST":
        session["myRoles"] = listStringtoInt(request.form.getlist('myRoles'))
        initGameData(session["myRoles"])
    return redirect(url_for('show_index'))

@app.route('/Delete',methods=["POST"])
def setOthersChara():
    if request.method == "POST":
        charaOfPlayerA = []
        charaOfPlayerB = []
        for i in range(8):
            session['A'+str(i+1)] = request.form.get('A'+str(i+1))
            charaOfPlayerA.append(session['A'+str(i+1)])
            session["B"+str(i+1)] = request.form.get('B'+str(i+1))
            charaOfPlayerB.append(session["B"+str(i+1)])
        deleteGameData(charaOfPlayerA,charaOfPlayerB)
    # return render_template('test.html',test1=charaOfPlayerA,test2=charaOfPlayerB)
    return redirect(url_for('show_index'))

@app.route('/',methods=["POST"])
def restartGame():
    if request.method == "POST":
        for i in range(8):
            session['A'+str(i+1)] = "Null"
            session["B"+str(i+1)] = "Null"
        session["myRoles"] = []
    delList = s_data_prospace.query.all()
    delDB(delList)
    return redirect(url_for('show_index'))