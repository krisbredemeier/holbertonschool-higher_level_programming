import threading
# import ip2country
import urllib2
import json

lock = threading.Lock()
class IPThread(threading.Thread):
    def __init__(self, ip, callback):
        threading.Thread.__init__(self)
        self.ip = ip
        self.callback = callback
    def run(self):
        lock.acquire()
        page = urllib2.urlopen('https://api.ip2country.info/ip?'+self.ip)
        content = page.read()
        txt_file = open('file.json', 'w')
        txt_file.write(content)
        txt_file.close()
        with open('file.json') as json_file:
            json_data = json.load(json_file)
        name_country = json_data['countryName']
        self.callback(name_country)
        lock.release()
