#!/usr/bin/python

import urllib2
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 5c6c68c5ed0e2184e7abf0d742de9f56e6953d61'
}

def printResults(data):
    theJSON = json.loads(data)


    with open('/tmp/34', 'w') as outfile:
        json.dump(theJSON, outfile)

def main():
    urlData = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"


    #open URL and read data
    webUrl = urllib2.urlopen(urlData)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        #prints customized results
        printResults(data)
        print "The file was saved!"
    else:
        print "receive error" + str(webUrl.getcode())

if __name__ == "__main__":
  main()
