import json
import tone
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def gettweets(search):
	ACCESS_TOKEN = '2410350192-xGB0lkWQnldWjzfurz9LObj0G9aVjRemGv0WEVQ'
	ACCESS_SECRET = 'nQswQILuWv9vLucpKoOifxDecADU1tBwWiNvTrokVD65D'
	CONSUMER_KEY = '8iviA4RjIdLCn49GF9uPPdZIZ'
	CONSUMER_SECRET = 'IeQFv7izGOjf4d1m50wLM0GQMA6PlD3mKyVQc0gVVlSLTEpgGx'

	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

	twitter = Twitter(auth=oauth)
	tweets = []
	a = twitter.search.tweets(q=search, result_type='popular', lang='en', count=15)
	for i in a["statuses"]:
		tweets.append([i["text"],tone.gettone(i["text"])])
	return tweets
