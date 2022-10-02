import mysql.connector 

mydb = mysql.connector.connect(
    host = "us-cdbr-east-06.cleardb.net",
    user = "bc5a1309c25640",
    passwd = "5ac8cc8a!"
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE heroku_6590fc27bd6e3bf")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)


# mysql://bc5a1309c25640:5ac8cc8a@us-cdbr-east-06.cleardb.net/heroku_6590fc27bd6e3bf?reconnect=true