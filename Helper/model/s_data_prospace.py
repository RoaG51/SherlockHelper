# -*- coding: utf-8 -*-
from Helper import db

class s_data_prospace(db.Model):
    __tablename__ = 's_data_prospace'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    A1 = db.Column(db.Integer)
    A2 = db.Column(db.Integer)
    A3 = db.Column(db.Integer)
    A4 = db.Column(db.Integer)
    A5 = db.Column(db.Integer)
    A6 = db.Column(db.Integer)
    A7 = db.Column(db.Integer)
    A8 = db.Column(db.Integer)
    B1 = db.Column(db.Integer)
    B2 = db.Column(db.Integer)
    B3 = db.Column(db.Integer)
    B4 = db.Column(db.Integer)
    B5 = db.Column(db.Integer)
    B6 = db.Column(db.Integer)
    B7 = db.Column(db.Integer)
    B8 = db.Column(db.Integer)
    C = db.Column(db.Integer)


    def __init__(self,A1=0,A2=0,A3=0,A4=0,A5=0,A6=0,A7=0,A8=0,B1=0,B2=0,B3=0,B4=0,B5=0,B6=0,B7=0,B8=0,C=0):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.A5 = A5
        self.A6 = A6
        self.A7 = A7
        self.A8 = A8
        self.B1 = B1
        self.B2 = B2
        self.B3 = B3
        self.B4 = B4
        self.B5 = B5
        self.B6 = B6
        self.B7 = B7
        self.B8 = B8
        self.C = C

    def __repr__(self):
        return '<s_data_prospace %r>' % self.id