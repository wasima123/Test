import mysql.connector as conn
mydb = conn.connect(host = "localhost", user ="root" , passwd = "123456789" )
print(mydb)
