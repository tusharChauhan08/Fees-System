import mysql.connector
database=mysql.connector.connect(host="localhost", user="root", password="", database="feesystem")
cursorObj=database.cursor()