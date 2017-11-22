# -*- coding: utf-8 -*-
from Helper import app,db
from Helper.model.s_3p_minfo import s_3p_minfo
from Helper.model.s_3p_ainfo import s_3p_ainfo
from Helper.model.s_3p_binfo import s_3p_binfo
from flask import render_template,request,session,url_for,redirect
from innerFunctions import initGameData,showMurderer,setPlayerChara,listStringtoInt,deleteGameData,delDB,quickAna


@app.route('/')
def show_index():
    if session.has_key('myRoles'):
        myChara = setPlayerChara(session["myRoles"])
    else:
        myChara = setPlayerChara()
    myResults = showMurderer(s_3p_minfo)
    curNum = s_3p_minfo.query.count()
    if curNum <= 10:
        myGameDatas = s_3p_minfo.query.order_by(s_3p_minfo.C).all()[0:10]
        charaOfPlayerA = []
        charaOfPlayerB = []
        charaOfPlayerM = []
        AnaResults = []
        for i in range(8):
            charaOfPlayerM.append(session['M' + str(i + 1)])
            charaOfPlayerA.append(session['A' + str(i + 1)])
            charaOfPlayerB.append(session["B" + str(i + 1)])
        for i in range(len(myGameDatas)):
            myGameData = s_3p_minfo.query.order_by(s_3p_minfo.C).all()[i]
            roleOfA=(myGameData.AR1,myGameData.AR2,myGameData.AR3,myGameData.AR4)
            roleOfB=(myGameData.BR1,myGameData.BR2,myGameData.BR3,myGameData.BR4)
            AnaResults.append([quickAna(s_3p_ainfo,roleOfA,charaOfPlayerB,charaOfPlayerM),quickAna(s_3p_binfo,roleOfB,charaOfPlayerM,charaOfPlayerA)])
        db.session.commit()
        db.session.close()
    else:
        AnaResults = [[[u"暂不显示", u"暂不显示", u"暂不显示"], [u"暂不显示", u"暂不显示", u"暂不显示"]]] * 10
    myGameDatas = s_3p_minfo.query.order_by(s_3p_minfo.C).all()[0:10]
    return render_template('index.html',myChara = myChara, results = myResults,gameDatas = myGameDatas,curNum = curNum,AnaResults=AnaResults)

@app.route('/Init',methods=["POST"])
def initMyRoles():
    if request.method == "POST":
        session["myRoles"] = listStringtoInt(request.form.getlist('myRoles'))
        initGameData(session["myRoles"],s_3p_minfo)
    return redirect(url_for('show_index'))

@app.route('/Delete',methods=["POST"])
def setOthersChara():
    if request.method == "POST":
        charaOfPlayerA = []
        charaOfPlayerB = []
        for i in range(8):
            session["M" + str(i + 1)] = request.form.get('M' + str(i + 1))
            session['A'+str(i+1)] = request.form.get('A'+str(i+1))
            charaOfPlayerA.append(session['A'+str(i+1)])
            session["B"+str(i+1)] = request.form.get('B'+str(i+1))
            charaOfPlayerB.append(session["B"+str(i+1)])
        deleteGameData(charaOfPlayerA,charaOfPlayerB,s_3p_minfo)
    return redirect(url_for('show_index'))

@app.route('/',methods=["POST"])
def restartGame():
    if request.method == "POST":
        for i in range(8):
            session['A'+str(i+1)] = "Null"
            session["B"+str(i+1)] = "Null"
            session["M" + str(i + 1)] = "Null"
        session["myRoles"] = []
        delList = s_3p_minfo.query.all()
        delDB(delList)
    return redirect(url_for('show_index'))

@app.route('/SOS')
def SOS():
    for i in range(8):
        session['A'+str(i+1)] = "Null"
        session["B"+str(i+1)] = "Null"
        session["M" + str(i + 1)] = "Null"
    session["myRoles"] = []
    delList = s_3p_minfo.query.all()
    delDB(delList)
    return redirect(url_for('show_index'))