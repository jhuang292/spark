#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import OAuthHandler, Stream


# In[ ]:


from tweepy.streaming import StreamListener
import socket
import json


# In[ ]:


consumer_key = 'JWSgJ9k2mAwKVPj4b91HW5N5i'
consumer_secret = 'DZi2ySuZpkCOTMYXntcvE65hvMC3XOSjdMJjmFMFwzzcA8DzdA'
access_token = '1168567400280858626-VZWBIMc3SCT020towCodeXUq9fnjGr'
access_secret = 'kvXItWgW5hne7fOINYgdGA4j7JWUgI6DaP0sepC8zZcGS'


# In[ ]:


class TweetListender(StreamListener):
    
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("ERROR ", e)
        return True
    
    def on_error(self, status):
        print(status)
        return True


# In[ ]:


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetListender(c_socket))
    twitter_stream.filter(track=['guitar'])


# In[ ]:


if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 9998
    s.bind((host, port))
    
    print('listening on port 9998')
    
    s.listen(5)
    c, addr = s.accept()
    
    sendData(c)


# In[ ]:




