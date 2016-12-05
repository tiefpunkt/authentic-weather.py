#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, requests, random
from config import *

URL="https://api.darksky.net/forecast/%s/%s,%s?units=si" % (API_KEY,LAT,LON)
r = requests.get(URL)
r.status_code
r.json()

with open('phrases.json') as f:
	phrases = json.load(f)

data = r.json()

temperature = data["currently"]["temperature"]

s1 = data["currently"]["icon"]
s1 = s1.replace("-", "_")
s1 = s1.replace("day", "")
s1 = s1.replace("night", "")
s1 = s1.replace("_", " ")
s1 = s1.strip()

selected_phrases = []

for phrase in phrases["phrases"]:
	if "condition" not in phrase or s1 == phrase["condition"]:
		if "max" not in phrase or temperature < phrase["max"]:
			if "min" not in phrase or temperature > phrase["min"]:
				selected_phrases.append(phrase)

#print selected_phrases
phrase = random.choice(selected_phrases)
print "%s °C" % temperature
print data["hourly"]["summary"]
print phrase["title"].replace("|", " ")
print phrase["subline"]
