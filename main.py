#!/usr/bin/env python

from __future__ import print_function, unicode_literals

import os, sys, subprocess
from flask import Flask, send_from_directory


app = Flask(__name__)
app.config['DEBUG'] = True
here = os.getcwd()

@app.route('/')
def hello():
    return send_from_directory('statics', 'main.html')

@app.route('/f')
def forward():
    try:
        out = subprocess.check_output(os.path.join(here, 'drive.sh f'), shell=True)
    except subprocess.CalledProcessError as e:
        return 'NG: ' + unicode(e)
    return 'OK'

@app.route('/s')
def stop():
    try:
        out = subprocess.check_output(os.path.join(here, 'drive.sh s'), shell=True)
    except subprocess.CalledProcessError as e:
        return 'NG: ' + unicode(e)
    return 'OK'

@app.route('/b')
def back():
    try:
        out = subprocess.check_output(os.path.join('drive.sh b'), shell=True)
    except subprocess.CalledProcessError as e:
        return 'NG: ' + unicode(e)
    return 'OK'

@app.route('/statics/<path:path>')
def statics(path):
    return send_from_directory('statics', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

