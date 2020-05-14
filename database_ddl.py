import datetime
from datetime import date
def ddl_db(i,file_obj):
    statement = 'create database ' + i + ';'
    file_obj.write(statement)
    return file_obj