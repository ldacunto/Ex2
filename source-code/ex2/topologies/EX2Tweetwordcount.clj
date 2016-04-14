(ns EX2Tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn EX2Tweetwordcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          )
    }
    ;; bolt configuration
    {"parse-tweet-bolt" (python-bolt-spec
          options
		  {"tweet-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["word"]
          :p 1
          )
     "count-bolt" (python-bolt-spec
          options
		  {"parse-tweet-bolt" ["word"]}
          "bolts.wordcount.WordCounter"
          ["word" "count"]
          :p 1
          )
    }
  ]
)
