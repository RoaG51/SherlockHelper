# -*- coding: utf-8 -*-
from Helper import app

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run( )