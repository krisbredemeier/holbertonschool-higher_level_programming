#!/usr/bin/env python

import urllib2
import json



def get_json(url):
    response = urllib2.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)
    commits = data[0]['commit']

    for commit in commits:
        print commit['commit']

url= "https://api.github.com/repos/holbertonschool/Betty/commits"
print(get_json(url))
z

# curl -i https://github.com/holbertonschool/Betty
