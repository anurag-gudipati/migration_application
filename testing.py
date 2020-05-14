from flask import Flask, render_template, request
from wtforms import TextField, Form

import mysql.connector
import re
from pymongo import MongoClient
mon_connection = MongoClient("mongodb://sample:root@cluster0-shard-00-00-nkket.mongodb.net:27017,cluster0-shard-00-01-nkket.mongodb.net:27017,cluster0-shard-00-02-nkket.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
''''''
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
for i in fet_table_names:
    #print(str(i))
    mon_collection = mon_db[str(i)]
    statement = "describe " + re.sub('[\[\'\]]','',str(list(i)))+";"
    print(statement)
    cursor.execute(statement)
    fet_column_names = cursor.fetchall()
    col_names=[]
    for j in fet_column_names:
        col_names.append(j[0])
    statement = "select *from "+ re.sub('[\[\'\]]','',str(list(i)))+";"
    cursor.execute(statement)
    values = cursor.fetchall()
    for k in values:
        temp_dict = dict(zip(col_names,k))
        if (i == ('address',)):
            temp_dict['location'] = 1
        if(i == ('film',)):
            print(temp_dict)
        #x = mon_collection.insert_one(temp_dict)
        #print(x.inserted_id)
        #print(temp_dict)
    col_names=[]

''' Flask Starts'''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Migration Application'


# for main page
@app.route('/')
def index():
    return render_template('index.html')

# for source database

# for target database
@app.route('/target_db', methods = ['POST','GET'])
def target_db():


    return render_template('target_db.html')
app.run(debug=True)






