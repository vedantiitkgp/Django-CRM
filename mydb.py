import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

# Prepare a cursor Object
cursorObj = dataBase.cursor()
cursorObj.execute("CREATE DATABASE testdb")

print("All done")