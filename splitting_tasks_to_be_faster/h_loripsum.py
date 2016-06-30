''' downloads a random paragraph of loripsum and saves to file '''

import threading
import urllib2

lock = threading.Lock()
class LoripsumThread(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename
    def run(self):
        ''' first basic method of lock '''
        lock.acquire()
        url = urllib2.urlopen('http://loripsum.net/api/1/short')
        read = url.read()
        txt_file = open(self.filename, 'aw')
        txt_file.write(read)
        txt_file.close()
        ''' second basic method of lock '''
        lock.release()
