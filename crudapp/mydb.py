import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234abcdEF'
)

# prepeare a cursor object

cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE demobank")

print("database demobank is created!")