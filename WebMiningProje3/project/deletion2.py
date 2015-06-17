#!/usr/bin/python

import json
import re
rate=json.load(open("anasayfa1.json"))

#for anasayfa.json
for j in range(0,20):
	for i in xrange(len(rate)):
	   if rate[i]["isim"]=="Coronation Street": 
			del rate[i]
			
			break

open("anasayfa2.json","w").write(
    json.dumps(rate,sort_keys=True,indent=4,separators=(',',':')))
	

rate2=json.load(open("anasayfa2.json"))
print len(rate2)
