import pymongo
import datetime
import re
from bson import code, Code
from datetime import date
from values_dml import dml_val
from tables_ddl import ddl_tb
from database_ddl import ddl_db
import mysql.connector
from pymongo import MongoClient
from datetime import date
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

source_DB=""
target_DB=""
host=""
user=""
passwd=""
dbname=""
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    error = ""
    if request.method == 'POST':
        source_DB = request.form['Source']
        target_DB = request.form['Target']
        #print(source_DB,target_DB)

    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('abou.html', title='About')


@app.route("/sql", methods=['GET', 'POST'])
def sq():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        host = request.form['host']
        user = request.form['User']
        passwd = request.form['password']
        dbname = request.form['DBName']
        #print(host,user,passwd,dbname)
        if len(host) == 0 or len(user) == 0 or len(passwd) == 0 or len(dbname) == 0:
            error = "Please fill all the fields"

    return render_template('SQ.html', title='SQL', message=error)


@app.route("/mongo", methods=['GET', 'POST'])
def md():
    error = ""
    if request.method == 'POST':
        url = request.form['URL']
        #dbname = request.form['DBName']
    return render_template('MDB.html', title='mongo', message=error)




''' For running the web application'''
if __name__ == "__main__":
    app.run(debug=True)

''' for mysql database'''
mysql_connection = mysql.connector.connect(
  host='127.0.0.1',
  user="root",
  passwd="India")
cursor = mysql_connection.cursor()
result = cursor.fetchall()
for i in range(len(result)):
    print(result[i])


# for mongo database
mon_connection = MongoClient("mongodb://sample:root@cluster0-shard-00-00-nkket.mongodb.net:27017,cluster0-shard-00-01-nkket.mongodb.net:27017,cluster0-shard-00-02-nkket.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
total_db = mon_connection.list_database_names()
''' ENDS HERE'''

''' SQL TO MONGO STARTS HERE'''
mysql_connection = mysql.connector.connect(
  host='127.0.0.1',
  user="root",
  passwd="India",
  database="sakila")
mon_db = mon_connection["temp_sakila"]
cursor = mysql_connection.cursor()
cursor.execute("show tables")
fet_table_names = cursor.fetchall()
print(fet_table_names)
li = list(fet_table_names)
#for  creating database in mongo db'''
db=mon_connection['sakila']
'''end here '''



''' For Mongo to SQL Database'''
# for creating all the databases in a cluster
if(source_DB == "SQL"):
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
elif(source_DB=="Mongo"):
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







