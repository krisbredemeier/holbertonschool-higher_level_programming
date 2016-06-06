while :
do
curl 'http://173.246.108.142/level1.php' -H 'Cookie: HoldTheDoor=1234' -H 'Connection: keep-alive' --data 'id=34&holdthedoor=Submit&key=1234' --compressed
done
