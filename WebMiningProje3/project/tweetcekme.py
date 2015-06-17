# -*- coding: utf-8 -*-
import time
from twython import Twython 
from twython.exceptions import TwythonRateLimitError
from twython import TwythonStreamer
import json

APP_KEY = 'QeB6C8DMGgijCjDZxhj7elRmp'
APP_SECRET = 'ywRsVM79ueJb5v691oOLtA5Zp4tonVLnpD7j37gReihOtWJohI'

"""
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
"""

OAUTH_TOKEN = "467479343-ZztPuihdcdyD03IYJQ2wb5Bf5JQLZuz2KhJxErwL"
OAUTH_TOKEN_SECRET = "oeLqafEU3yoCUL3YNhCz9EbStS0lnqc0k1ZpwvxWAp41x"


print OAUTH_TOKEN
print OAUTH_TOKEN_SECRET
veri=[]
class MyStreamer(TwythonStreamer):
    cnt = 0
    
    
    def on_success(self, data):
        
        
        tweetler={'tweet':''}
        
        if 'text' in data:
            print "TEXT = %s" % data['text'].encode('utf-8')
       
        tweetler={'tweet':data['text'].encode('utf-8')}
        veri.append(tweetler)
        place = data.get('place')     
        # print type(place)
        geo = data.get("geo")
        #print veri
        
 
        print"\n\n---------------------------------------------\n\n" 
        self.cnt += 1
		
        if (self.cnt == 1000): self.disconnect()
        
    def on_error(self, status_code, data):
        print status_code
        print data
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()
        
        
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
                    
stream.statuses.filter(track='Game of Thrones,Arrow,Vampire Diaries,Grey''s Anatomy,Supernatural,Once upon a time,The Blacklist,The 100,Castle,NCIS,The Good Wife,Revenge,How I met your mother,Marvel Agent''s of SHIELD,the Big Bang Theory,Vikings,Criminal Minds,Bones')
with open('tweetler.json', 'w') as outfile:
    json.dump(veri, outfile)
print "DISCONNECTED"
        
