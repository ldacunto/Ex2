import tweepy

consumer_key = "5dxu6rBs61iN0ZzMrtIDXSu0M";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "hpQNJWQFmdI1dVwE3RCOcZbsXUgaPxVUYg3sQVuVvY6OjmBq2k";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "144461925-xYH3a6xewz10eWs5VypP3G4s0qhRgdVvoq1oFMw5";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "XycdPqPYfeJYZtUINKy70RGhlIMou7QukrVT5Ae3pCMZt";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



