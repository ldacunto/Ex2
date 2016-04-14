import psycopg2
import sys
try:
	conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	if len(sys.argv)>1:
		range = sys.argv[1]
		k = range.split(",")
		cur.execute("SELECT word, count from Tweetwordcount WHERE count >= %s and count <= %s order by count desc;" %(k[0],k[1]))
		records = cur.fetchall()
		for result in records:
		    print "%s : %s" %(result[0], result[1])
			
		result = cur.fetchone()
	else:
		print "Missing k1 and k2"
	conn.commit()
	conn.close()
except:
    print "Problems Retrieving data"

