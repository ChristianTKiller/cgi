#!C:/Python311/python.exe
#import mysql.conector
import os
import cgi
import cgitb 
cgitb.enable()
print("Content-type: text/html")
print()
print("<h1>Consulta Usuarios</h1>")

con =mysql.conector.conect(user = 'root', password = '', host = '127.0.0.1', database = 'foro')
sql = ("SELECT * FROM users")
cursor = con.cursor()
cursor.executable(sql)
for (email, password, name, avatar, role) in cursor: 
    print("{},{},{},{},{},".fprmat(email, password, name, avatar, role))