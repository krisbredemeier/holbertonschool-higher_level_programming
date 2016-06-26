import threading

class ReverseStrThread(threading.Thread):
    sentence = ""
    def __init__(self, word):
        if not isinstance (word, str):
            raise Exception("word is not a string")
        self.word = word
        threading.Thread.__init__(self)

    def run(self):
        with threading.Lock():
            ReverseStrThread.sentence = ReverseStrThread.sentence + (self.word[::-1]) + " "
