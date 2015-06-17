# -*- coding: utf-8 -*-
import fileinput


for line in fileinput.input('episode1.json', inplace=True):
    print(line.replace("\\r", ""))
for line in fileinput.input('episode1.json', inplace=True):
    print(line.replace("\\n", ""))
for line in fileinput.input('episode1.json', inplace=True):
    print(line.replace("\\t", ""))
for line in fileinput.input('anasayfa1.json', inplace=True):
    print(line.replace("\\n", ""))
	
for line in fileinput.input('oyuncular1.json', inplace=True):
    print(line)

