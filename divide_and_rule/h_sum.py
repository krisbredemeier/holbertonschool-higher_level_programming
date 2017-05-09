import threading

class SumThread(threading.Thread):
    def __init__(self, n):
        self.n = n
        if not isinstance (n, list):
            raise Exception("numbers is not an array of integers")
        threading.Thread.__init__(self)

    def run(self):
        with threading.Lock():
            Sum.totoal += sum(self.n)

class Sum():
    total = 0
    def __init__(self, nb_threads, integers):
        self.nb_threads = nb_threads
        self.integers = integers
        if not isinstance (nb_threads, int):
            raise Exception("nb_threads is not an integer")
        if not isinstance (integers, list) or not all(isinstance(integers, int) for i in integers):
            raise Exception("numbers is not an array of integers")

    def isComputing(self):
        if threading.activeCount() == 1:
            return False
        else:
            return True

    def __str__(self):
        with threading.Lock():
            return str(Sum.total)
