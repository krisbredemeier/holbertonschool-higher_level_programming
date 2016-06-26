import threading

class OrderedArrayThread(threading.Thread):
    def __init__(self, number):
        self.number = number
        if not isinstance(number, int):
            raise Exception("number is not an integer")
        threading.Thread.__init__(self)
    list = []
    def run(self):
        with threading.Lock():
            OrderedArrayThread.list.append(self.number)
            OrderedArrayThread.list.sort()

class OrderedArray():
    def __init__(self):
        pass

    def add(self, number):
        if not isinstance(number, int):
            raise Exception("number is not an integer")
        OrderedArrayThread(number).start()

    def isSorting(self):
        if threading.activeCount() == 1:
            return False
        else:
            return True

    def __str__(self):
        with threading.Lock():
            return str(OrderedArrayThread.list)
