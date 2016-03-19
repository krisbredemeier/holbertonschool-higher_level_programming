#!/usr/bin/ruby
require 'rubygems'
require 'json'
require 'pp'


#file = File.read('ruby.json')
#data_hash = JSON.parse('ruby.json')
json = File.read('ruby.json')
obj = JSON.parse(json)


pp obj






#extheaders = {
#  'User-Agent' => 'Holberton_School',
#  'Authorization' => 'token 5c6c68c5ed0e2184e7abf0d742de9f56e6953d61'
#}
