import re
from datetime import date

import mysql.connector
from flask import Flask, render_template, request
from pymongo import MongoClient

from database_ddl import ddl_db
from tables_ddl import ddl_tb
from values_dml import dml_val

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    error = ""
    print('get operation in home')
    if request.method == 'POST':
        home.source_DB = request.form['Source']
        home.target_DB = request.form['Target']
        print(home.source_DB)
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('abou.html', title='About')


@app.route("/sql", methods=['GET', 'POST'])
def sq():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        sq.host = request.form['host']
        sq.user = request.form['User']
        sq.passwd = request.form['password']
        sq.dbname = request.form['DBName']
        print(sq.host, sq.user, sq.passwd, sq.dbname)
        if len(sq.host) == 0 or len(sq.user) == 0 or len(sq.passwd) == 0 or len(sq.dbname) == 0:
            error = "Please fill all the fields"

    return render_template('SQ.html', title='SQL', message=error)


@app.route("/mongo", methods=['GET', 'POST'])
def md():
    error = ""
    if request.method == 'POST':
        md.url = request.form['URL']
        print(md.url)
        #dbname = request.form['DBName']
    return render_template('MDB.html', title='mongo', message=error)

@app.route('/thank')
def json():
    return render_template('thank.html')


#background process happening without any refreshing
@app.route('/background_process_test')
def migration_start():
    print(home.source_DB)
    print(sq.host)
    print(md.url)

    ''' For running the web application'''
if __name__ == "__main__":
    app.run(debug=True)


'''Mongo and SQL'''





''' For Mongo to SQL Database'''
# for creating all the databases in a cluster







