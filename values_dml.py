import datetime
from datetime import date
def dml_val(db_name, collection_name, all_docs,file_obj):
    today = date.today()
    for i in all_docs:
        statement = 'Insert into ' + db_name + '.' + collection_name + ' columns('
        col_names=list(i.keys())
        col_values=list(enumerate(i.keys(),0)) #i.values()#enumerate(i.keys(),0)
        final_col_names = ','.join(map(str,col_names))
        final_col_values= '"' + '","'.join(map(str,col_values)) + '"'  #lambda str1: str(str1).replace("\\"," ")
        statement = statement + final_col_names + ') values(' + final_col_values + ');\n'
        file_obj.write(statement)
        statement = ' '




#li = '"' + '","'.join(map(str,s)) + '"'
