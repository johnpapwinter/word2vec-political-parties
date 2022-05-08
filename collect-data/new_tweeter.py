import tweepy #https://github.com/tweepy/tweepy
#import csv

#Twitter API credentials
consumer_key = "zNsQJuQ4jbQ8NWFUD49G6OXhO"
consumer_secret = "rYwIlwYOq24BR2ioaCLHZOndFDUrbftibrka4xPB8NjRemR1yB"
access_key = "1878517706-9lFR0RIYtluCEuveI0McH3UScLjuQv6bbKAYheH"
access_secret = "zW48PEvliWT0VMzis2jlRGkVNkchVlJj7LKfap4yeI9bH"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#screen_name = "@PrimeministerGR"



alltweets = []

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name = screen_name,count=200)


#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1


#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
	print ("getting tweets before %s" % (oldest))
	
	#all subsiquent requests use the max_id param to prevent duplicates
	new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#update the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	print ("...%s tweets downloaded so far" % (len(alltweets)))


#transform the tweepy tweets into a 2D array that will populate the csv	
#outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
#outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
outtweets = [[tweet.created_at, tweet.text] for tweet in alltweets]

f = open('%s_tweets.txt' % screen_name, 'a', encoding='utf-8')
for tweet in outtweets:
    f.write(str(tweet))
    f.write('\n')
f.close()

#write the csv	
#with open('%s_tweets.csv' % screen_name, 'w', encoding='utf-8') as f:
#	writer = csv.writer(f)
#	writer.writerow(["id","created_at","text"])
#	writer.writerows(outtweets)

