#!/usr/bin/env python

import urllib2
import json



def get_json(url):
    response = urllib2.urlopen(url)
    data = response.read().decode("utf-8")
    commits = json.loads(data)

    # print commits

    for commit in commits:
        print (commit.get('sha'))

url= "https://api.github.com/repos/holbertonschool/Betty/commits"
print(get_json(url))

# curl -i https://github.com/holbertonschool/Betty
