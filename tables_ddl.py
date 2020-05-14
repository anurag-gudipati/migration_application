
def ddl_tb(db_name, file_obj, collection_name, all_docs):
    write_statement = '\ncreate table ' + db_name+'.' +collection_name + '('
    col_names= set()
    for i in all_docs:
        col_names = col_names | set(i.keys())
    col_names=list(col_names)
    col_statement = ' '
    for j in col_names:
        col_statement = col_statement + j + ' varchar(1000),'
    col_statement = col_statement[:-1] + ');'
    write_statement = write_statement + col_statement
    file_obj.write(write_statement)


