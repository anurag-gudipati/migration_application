import mysql.connector
mysql_connection = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        passwd="India")
cursor = mysql_connection.cursor()
result = cursor.fetchall()
for i in range(len(result)):
    print(result[i])
