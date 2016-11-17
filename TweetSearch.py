import sys
from twython import Twython
i=0

#ENTER USER KEYS KEY HERE
TWITTER_APP_KEY = 'XXXXXXXXXXXXXXXXXXXXX'
TWITTER_APP_KEY_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXX' 
TWITTER_ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
TWITTER_ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXX'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q=sys.argv[1],   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  if "RT" in tweet['text']:
  	pass
  else:
  	print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
  	i=i+1

print 'Number of tweets: ', i
