# -*- coding: utf-8 -*-
from Helper import db
import itertools

def setPlayerChara(roleList=[]):
    roleChara = (
        (0, 0, 1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 1, 0, 1),
        (0, 0, 0, 1, 1, 0, 1, 0),
        (0, 0, 1, 1, 1, 0, 0, 0),
        (0, 1, 0, 1, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0, 0, 0),
        (1, 0, 0, 1, 0, 0, 1, 0),
        (1, 1, 1, 0, 0, 0, 0, 0),
        (1, 0, 1, 0, 0, 0, 1, 0),
        (1, 1, 0, 0, 1, 0, 0, 0),
        (1, 0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 1, 1, 0, 0),
        (0, 1, 0, 0, 0,0 , 0, 1)
    )
    results = [0,0,0,0,0,0,0,0]
    for role in roleList:
        for i in range(8):
            results[i] += roleChara[role][i]
    return results

def listStringtoInt(myStringList):
    myIntList = []
    for item in myStringList:
        myIntList.append(int(item))
    return myIntList

def subList(myList,myTuple):
    result = myList[:]
    for item in myTuple:
        result.remove(item)
    return result
def delDB(delList):
    for delitem in delList:
        db.session.delete(delitem)
    db.session.commit()
    db.session.close()
    return

def initGameData(myRoleTuple,sheet):
    delList = sheet.query.all()
    delDB(delList)
    roleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    roleList1 = subList(roleList,myRoleTuple)
    for rolesOfPlayerA in itertools.combinations(roleList1, 4):
        roleList2 = subList(roleList1, rolesOfPlayerA)
        for rolesOfPlayerB in itertools.combinations(roleList2, 4):
            roleList3 = subList(roleList2, rolesOfPlayerB)
            roleOfMurderer = roleList3[0]
            charaOfPlayerA = setPlayerChara(rolesOfPlayerA)
            charaOfPlayerB = setPlayerChara(rolesOfPlayerB)
            newitem = sheet(A1=charaOfPlayerA[0],A2= charaOfPlayerA[1], A3=charaOfPlayerA[2],A4=charaOfPlayerA[3],
                            A5=charaOfPlayerA[4],A6= charaOfPlayerA[5], A7=charaOfPlayerA[6],A8=charaOfPlayerA[7],
                            B1=charaOfPlayerB[0], B2=charaOfPlayerB[1], B3=charaOfPlayerB[2],B4=charaOfPlayerB[3],
                            B5=charaOfPlayerB[4], B6=charaOfPlayerB[5], B7=charaOfPlayerB[6],B8=charaOfPlayerB[7],
                            AR1=rolesOfPlayerA[0], AR2=rolesOfPlayerA[1], AR3=rolesOfPlayerA[2], AR4=rolesOfPlayerA[3],
                            BR1=rolesOfPlayerB[0], BR2=rolesOfPlayerB[1], BR3=rolesOfPlayerB[2], BR4=rolesOfPlayerB[3],
                            C=roleOfMurderer)
            db.session.add(newitem)
    db.session.commit()
    db.session.close()
    return

def deleteGameData(charaOfPlayerA,charaOfPlayerB,sheet):
    for i in range(len(charaOfPlayerA)):
        if charaOfPlayerA[i] == 'Exist':
            delList = sheet.query.filter(getattr(sheet,"A"+str(i+1)) == 0).all()
            delDB(delList)
        elif charaOfPlayerA[i] <= '5'and charaOfPlayerA[1] >= '0':
            delList = sheet.query.filter(getattr(sheet,"A"+str(i+1)) != int(charaOfPlayerA[i] )).all()
            delDB(delList)
    for i in range(len(charaOfPlayerB)):
        if charaOfPlayerB[i] == 'Exist':
            delList = sheet.query.filter(getattr(sheet,"B"+str(i+1)) == 0).all()
            delDB(delList)
        elif charaOfPlayerB[i] <= '5'and charaOfPlayerB[i] >= '0':
            delList = sheet.query.filter(getattr(sheet,"B"+str(i+1)) != int(charaOfPlayerB[i] )).all()
            delDB(delList)
    return

def showMurderer(sheet):
    results = [
        [u"塞巴斯蒂安·莫蓝",0],
        [u" 艾琳·艾德勒", 0],
        [u"雷斯垂德探长", 0],
        [u"格雷格森探长", 0],
        [u"贝恩斯探长", 0],
        [u"布莱斯萃探长", 0],
        [u"霍普金斯探长", 0],
        [u"夏洛克·福尔摩斯", 0],
        [u"约翰·华生", 0],
        [u"麦克罗夫特·福尔摩斯", 0],
        [u"哈德逊夫人", 0],
        [u"玛丽·莫斯坦", 0],
        [u"詹姆斯·莫里亚蒂", 0]
    ]
    totalNum = sheet.query.count()
    if totalNum == 0:
        return results
    for i in range (13):
        curNum = sheet.query.filter(sheet.C == i).count()
        results[i][1] = curNum/float(totalNum)
    return results

def quickAna(sheet,roleOfPlayerM,charaOfPlayerA,charaOfPlayerB):
    initGameData(roleOfPlayerM,sheet)
    deleteGameData(charaOfPlayerA,charaOfPlayerB,sheet)
    resultsList = sheet.query.all()
    murders = showMurderer(sheet)
    murderPro = []
    for murder in murders:
        if murder[1] != 0:
            murderPro.append(murder[1])
    if murderPro:
        murderMax = max(murderPro)
    else:
        murderMax = 0
    return [len(resultsList),len(murderPro),murderMax]