Download the project into your root directory

Software that must be installed in the server:
1. Python 2.7
2. Apache Storm
3. Postgresql

Libraries required:
1. tweepy. To install: pip install streamparse
2. streamparse. To install: pip install tweepy
3. pycopg. To install: pip install psycopg2

Credentials to access Twitter:
See https://apps.twitter.com for how to create an application.
Retrieve from the website:
- consumer_key
- consumer_secret
- access_token
- access_token_secret
And update the file /root/lab/Twittercredentials.py. Run hello-stream-twitter.py to test the credentials.
If it works, update the file  /root/lab/ex2/src/spout/tweets.py withthe credentials.

Postgresql:
In the server must be already installed Postgresql with standard installation (username postgres and port: 5432) and running.
Run psycopg-sample.py to create the database for the project and the table used in the lab.

How to run the software
Open a shell, go to /root/lab/ex2 and run the command "sparse run".
You will start to see a stream of words retrieved from Twitter.

Retrieve the data
After a while stop the software and run the script "python finalresults.py to" in the directory /root/lab/.
You will see something like "Total number of occurences of "to": 1725" with a different number.
Or run the command "python histogram.py 10,40" in hte same path.
You will see a list of words with the number of times that were retrieved from Twitter from 40 occurances to 10.