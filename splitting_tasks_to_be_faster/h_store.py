import threading
from time import sleep
from random import randint

lock = threading.Lock()
class Store():
    def __init__(self, item_number, person_capacity):
        # threading.Thread.__init__(self)
        self.item_number = item_number
        self.person_capacity = person_capacity
        self.nbpersoninside = 0
    def enter(self):
        ''' A semaphore manages an internal counter
        which is decremented by each acquire() call
        and incremented by each release() call '''
        semaphore = threading.BoundedSemaphore(self.person_capacity)
        semaphore.acquire()
        self.nbpersoninside += 1
        semaphore.release()
    def buy(self):
        ''' generate random int '''
        sleep(randint(5,10))
        if self.item_number > 0:
            self.item_number -= 1
        self.nbpersoninside -= 1
        if self.item_number <= 0:
            return False
        return True
