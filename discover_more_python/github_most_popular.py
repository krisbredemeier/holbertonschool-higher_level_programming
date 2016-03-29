
request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 5c6c68c5ed0e2184e7abf0d742de9f56e6953d61'
}

import urllib2
import json
req = urllib2.Request("https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print json
