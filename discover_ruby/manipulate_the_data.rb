#!/usr/bin/ruby
require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 5c6c68c5ed0e2184e7abf0d742de9f56e6953d61'
}

clnt = HTTPClient.new
file = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
parsed = JSON.parse(file)
parsed ["items"].map {|e| puts e["full_name"]}.join
