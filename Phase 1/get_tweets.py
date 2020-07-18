from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key="hWyJtfP1OuoMLWGyLHmF9QyTJ"
consumer_secret="DnxqOTqrkT9AbPFU5lKy4LvR1HqHFgiChYmZcSGXZgjJswCSre"
access_token="411485026-wau8Y5Jscj1mYPsmMhuX7E9zVhcpBXG5F6fh7hFR"
access_token_secret="4ChwOurh31igUftliyqtCW0soT5Wg3wbZsKUAAuJc9Qo4"

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            with open('data1.json', 'a') as outfile:
                json.dump(data,outfile)
            with open('data2.json','a') as outputj:
                outputj.write(data)
            with open('tweets_data.txt', 'a') as tweets:
                tweets.write(data)
                tweets.write('\n')
            outfile.close()
            tweets.close()
            outputj.close()
        except BaseException as e:
            print('problem collecting tweet',str(e))
        return True
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['BlackLivesMatter','AllLivesMatter'])
