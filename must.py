import mysql.connector

db =  mysql.connector.connect(host="localhost", # Host, usually localhost
                     user="root", # your username
                     password="mai123", # your password
                     db="must_student") # name of the data base
#create a Cursor object.
cur = db.cursor()

# Write SQL statement here
cur.execute("SELECT * FROM pharmacy  ;")

# print all the first and second cells of all the rows
for row in cur.fetchall() :
    print (row[0])