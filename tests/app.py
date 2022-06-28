
#from flask import Flask, jsonify, render_template, url_for, redirect
from flask import Flask, jsonify, render_template, request
import sqlite3
#from sqlalchemy import create_engine
#import pandas as pd
#import json


# DATABASE SETUP
###
#

# FLASK SETUP
###
#
app = Flask(__name__, template_folder='static', static_folder='static')


# ROUTES
###
#

# HTML PAGES
@app.route('/')
def html_index():
    return render_template('index.html')

@app.route('/assets')
def html_assets():
    return render_template('assets.html')

@app.route('/liabilities')
def html_liabilities():
    return render_template('liabilities.html')

@app.route('/info')
def html_info():
    return render_template('information.html')


# RUN APP
###
#
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)
