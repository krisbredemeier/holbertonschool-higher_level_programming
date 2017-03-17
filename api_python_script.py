#!/usr/bin/env python

import urllib2
import json

# url= "https://github.com/holbertonschool/Betty"
# response = urllib2.urlopen(url)
# data = json.loads(response.read())
# print data
# commits.
#     print "#{commit['date']}:#{commit['commit ID']['username']['commit message']}"

def get_json(url):
    response = urllib2.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url= "https://github.com/holbertonschool/Betty"
print(get_json(url))
