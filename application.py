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
    if(home.source_DB=="SQL"):
        mon_connection = MongoClient(md.url)
        ''''''
        mysql_connection = mysql.connector.connect(
            host=sq.host,
            user=sq.user,
            passwd=sq.passwd,
            database=sq.dbname)
        mon_db = mon_connection[sq.dbname]
        cursor = mysql_connection.cursor()
        cursor.execute("show tables")
        fet_table_names = cursor.fetchall()
        print(fet_table_names)
        li = list(fet_table_names)
        # for  creating database in mongo db'''
        db = mon_connection['sakila']
        '''end here '''
        for i in fet_table_names:
            # print(str(i))
            mon_collection = mon_db[str(i)]
            statement = "describe " + re.sub('[\[\'\]]', '', str(list(i))) + ";"
            print(statement)
            cursor.execute(statement)
            fet_column_names = cursor.fetchall()
            col_names = []
            for j in fet_column_names:
                col_names.append(j[0])
            statement = "select *from " + re.sub('[\[\'\]]', '', str(list(i))) + ";"
            cursor.execute(statement)
            values = cursor.fetchall()
            for k in values:
                temp_dict = dict(zip(col_names, k))
                if (i == ('address',)):
                    temp_dict['location'] = 1
                if (i == ('film',)):
                    print(temp_dict)
                # x = mon_collection.insert_one(temp_dict)
                # print(x.inserted_id)
                # print(temp_dict)
            col_names = []
    elif(home.source_DB=="Mongo"):
        ''' from Mongodb to mysql database '''
        mysql_connection = mysql.connector.connect(
            host=sq.host,
            user=sq.user,
            passwd=sq.passwd)
        cursor = mysql_connection.cursor()
        '''end here'''

        ''' Only Connection for Mongo'''
        mon_connection = MongoClient(
            "mongodb://sample:root@cluster0-shard-00-00-nkket.mongodb.net:27017,cluster0-shard-00-01-nkket.mongodb.net:27017,cluster0-shard-00-02-nkket.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
        total_db = mon_connection.list_database_names()
        '''End Here'''
        ''' This is for Mongo All Databases to SQL All Databases'''
        for i in total_db:
            if (i != 'admin' and i != 'local'):
                today = date.today()
                sample_name = i + '_ddl_' + str(today)
                f = open(r'C:\Users\Anurag\PycharmProjects\Temp\%s.sql' % sample_name, 'w')
                file_name = i + '_dml' + str(today)
                f1 = open(r'C:\Users\Anurag\PycharmProjects\Temp\%s.sql' % file_name, 'w')
                file_obj = ddl_db(i, f)
                db = mon_connection.get_database(i)
                collection_names = db.list_collection_names()
                for j in collection_names:
                    all_documents = db[j].find({})
                    ddl_tb(i, file_obj, j, all_documents)
                    all_documents = db[j].find({})
                    dml_val(i, j, all_documents, f1)
        ''' End Here For Mongo to SQL ALl Databases'''
    print(home.source_DB)
    print(sq.host)
    print(md.url)

    ''' For running the web application'''
if __name__ == "__main__":
    app.run(debug=True)


'''Mongo and SQL'''





''' For Mongo to SQL Database'''
# for creating all the databases in a cluster







