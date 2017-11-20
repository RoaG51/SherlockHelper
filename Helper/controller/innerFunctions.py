# -*- coding: utf-8 -*-
from Helper.model.s_data_prospace import s_data_prospace
from Helper import db
import itertools

def refreshProSpace(m1,m2,m3,m4):
    Allroles =(
        (0,0,1,0,0,0,0,1),
        (0,1,0,0,0,1,0,1),
        (0,0,0,1,1,0,1,0),
        (0,0,1,1,1,0,0,0),
        (0,1,0,1,0,0,0,0),
        (0,0,1,1,0,0,0,0),
        (1,0,0,1,0,0,1,0),
        (1,1,1,0,0,0,0,0),
        (1,0,1,0,0,0,1,0),
        (1,1,0,0,1,0,0,0),
        (1,0,0,0,0,1,0,0),
        (0,0,0,0,1,1,0,0),
        (0,0,0,0,0,1,0,1)
    )
    deletes = s_data_prospace.query.all()
    for deleteitem in deletes:
        db.session.delete(deleteitem)
    rolelist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    myroles = [m1, m2, m3, m4]
    for role in myroles:
        rolelist.remove(role)
    for Aroles in itertools.combinations(rolelist, 4):
        Arolelist = rolelist[:]
        for Arole in Aroles:
            Arolelist.remove(Arole)
        for Broles in itertools.combinations(Arolelist, 4):
            Brolelist = Arolelist[:]
            for Brole in Broles:
                Brolelist.remove(Brole)
            C = Brolelist[0]
            # A = []
            # B = []
            # for i in range(8)
            #     for j in range(3)
            # A1 = Allroles[Aroles[0]][0] + Allroles[Aroles[1]][0] + Allroles[Aroles[2]][0] + Allroles[Aroles[3]][0]
            # A2 = Allroles[Aroles[0]][1] + Allroles[Aroles[1]][1] + Allroles[Aroles[2]][1] + Allroles[Aroles[3]][1]
            # A3 = Allroles[Aroles[0]][2] + Allroles[Aroles[1]][2] + Allroles[Aroles[2]][2] + Allroles[Aroles[3]][0]
            # A4 = Allroles[Aroles[0]][3] + Allroles[Aroles[1]][3] + Allroles[Aroles[2]][3] + Allroles[Aroles[3]][0]
            # A5 = Allroles[Aroles[0]][4] + Allroles[Aroles[1]][4] + Allroles[Aroles[2]][4] + Allroles[Aroles[3]][0]
            # A6 = Allroles[Aroles[0]][5] + Allroles[Aroles[1]][5] + Allroles[Aroles[2]][5] + Allroles[Aroles[3]][0]
            # A7 = Allroles[Aroles[0]][6] + Allroles[Aroles[1]][6] + Allroles[Aroles[2]][6] + Allroles[Aroles[3]][0]
            # A8 = Allroles[Aroles[0]][7] + Allroles[Aroles[1]][7] + Allroles[Aroles[2]][7] + Allroles[Aroles[3]][0]
            newitem = s_data_prospace(A1=A1,
                                      A2=Aroles[1], A3=Aroles[2], A4=Aroles[3],
                                      B1=Broles[0],
                                      B2=Broles[1], B3=Broles[2], B4=Broles[3], C=C)
            db.session.add(newitem)
    db.session.commit()
    db.session.close()
    return
