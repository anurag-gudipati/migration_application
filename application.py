import pymongo
import datetime
from bson import code, Code
from datetime import date
from values_dml import dml_val
from tables_ddl import ddl_tb
from database_ddl import ddl_db
import mysql.connector
from pymongo import MongoClient
from datetime import date
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
###########################################

# for creating all the databases in a cluster
for i in total_db:
    if(i!='admin' and i!='local'):
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







