#!/usr/bin/ruby
require 'httpclient'
require 'json'

File.open('/tmp/34', 'w') do |file|
clnt = HTTPClient.new
file.puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
puts "The file was saved!"
end
