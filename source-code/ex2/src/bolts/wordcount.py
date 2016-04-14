from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import sys

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        
    def process(self, tup):
        word = tup.values[0]        
        # Increment the local count
        self.counts[word] += 1
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
        #Insert
        conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        cur.connection.set_isolation_level(0)
        if (self.counts[word] ==  1):
            try:
                cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES (%s, %s)", (word, self.counts[word]));
                conn.commit()
            except:
                cur.execute("UPDATE Tweetwordcount SET count=count+1 WHERE word=%s", [word])
                conn.commit()
        else:
        #Update
            cur.execute("UPDATE Tweetwordcount SET count=count+1 WHERE word=%s", [word])
            conn.commit()
        self.emit([word, self.counts[word]])