#!/usr/bin/python

import json
import re
oyuncu=json.load(open("oyuncular1.json"))
print len(oyuncu)


#for anasayfa.json
for j in range(0,55):
	for i in xrange(len(oyuncu)):
	   if oyuncu[i]["title"]=="Coronation Street": 
			del oyuncu[i]
			
			break

open("oyuncular2.json","w").write(
    json.dumps(oyuncu,sort_keys=True,indent=4,separators=(',',':')))
	

rate2=json.load(open("oyuncular2.json"))
print len(rate2)
