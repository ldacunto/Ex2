#Sample code snippets for working with psycopg
#Connecting to a database
#Note: If the database does not exist, then this command will create the database
import psycopg2
try:
    conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.connection.set_isolation_level(0)
    cur.execute("CREATE DATABASE Tcount")
    cur.close()
    conn.close()
    print "created database Tcount"
except:
    print "Not Created"

#Create a Table
#The first step is to create a cursor. 

#cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE Tweetwordcount(word TEXT PRIMARY KEY NOT NULL,count INT NOT NULL);''')
    conn.commit()
    conn.close()
    print "created table Tweetwordcount"
except:
    print "Not Created"

#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

cur = conn.cursor()

#Insert
cur.execute("INSERT INTO Tweetwordcount (word,count) \
      VALUES ('test', 1)");
conn.commit()

#Update
#Assuming you are passing the tuple (uWord, uCount) as an argument
uWord = 'test'
uCount = 10
cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (uCount, uWord))
conn.commit()

#Select
cur.execute("SELECT word, count from Tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
