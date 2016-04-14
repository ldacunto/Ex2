import psycopg2
import sys
try:
	conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	if len(sys.argv)>1:
		word = sys.argv[1]
		cur.execute("SELECT word, count from Tweetwordcount WHERE word = '%s';" %word)
		result = cur.fetchone()
		if (result is None):
			print "Total number of occurences of \"%s\": %s" %(word, 0)
		else:
			print "Total number of occurences of \"%s\": %s" %(result[0], result[1])
	else:
		cur.execute("SELECT word, count from Tweetwordcount order by word asc")
		records = cur.fetchall()
		for result in records:
		    print "(%s, %s)" %(result[0], result[1])
	conn.commit()
	conn.close()
except:
    print "Problems Retrieving data"

