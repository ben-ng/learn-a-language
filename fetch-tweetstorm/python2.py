#!/usr/bin/python

from argparse import ArgumentParser
import requests
from base64 import b64encode

p = ArgumentParser()
p.add_argument('consumer_key')
p.add_argument('consumer_secret')
p.add_argument('tweet_id')
args = p.parse_args()

class Twitter:
	def __init__(self, consumer_key, consumer_secret):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = ''

	def get_access_token(self):
		if self.access_token:
			return self.access_token
		
		url = 'https://api.twitter.com/oauth2/token'
		bearer_token = b64encode('%s:%s' % (self.consumer_key, self.consumer_secret))
		data = 'grant_type=client_credentials'
		headers = {
			'Authorization': 'Basic %s' % bearer_token,
			'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
		}
		resp = requests.post(url, data=data, headers=headers)
		self.access_token = resp.json().get('access_token')
		return self.access_token

	def get_tweet(self, tweet_id):
		url = 'https://api.twitter.com/1.1/statuses/show.json'
		r = requests.get(url, params={'id': tweet_id}, headers={'Authorization': 'Bearer %s' % self.get_access_token()})
		tweet = r.json()
		return {
			'id': tweet.get('id_str'),
			'reply_to_id': tweet.get('in_reply_to_status_id_str'),
			'screen_name': tweet.get('user', {}).get('screen_name'),
			'text': tweet.get('text'),
			'created_at': tweet.get('created_at')
		}
	
	def get_tweetstorm(self, last_tweet_id, tweetstorm = None):
		tweetstorm = tweetstorm if tweetstorm is not None else []

		if (last_tweet_id == None):
			return tweetstorm

		tweet = self.get_tweet(last_tweet_id)
		tweetstorm.append(tweet)
		return self.get_tweetstorm(tweet['reply_to_id'], tweetstorm)

client = Twitter(args.consumer_key, args.consumer_secret)

# reversed (and any of these that end with an 'ed') doesn't create a copy,
# it just reveres the order of iteration. enumerate lets us iterate over
# both the index and value, rather than just the value.
for idx, tweet in enumerate(reversed(client.get_tweetstorm(args.tweet_id))):
	if idx == 0:
		title = '@%s, at %s' % (tweet['screen_name'], tweet['created_at'])
		underline = '=' * len(title)
		print '%s\n%s\n' % (title, underline)
	
	print '%s\n' % tweet['text']
