import threading

class StrLengthThread(threading.Thread):
    total_str_length = 0;
    def __init__(self, word):
        self.word = word
        if not isinstance(word, str):
            raise Exception("word is not a string")
        threading.Thread.__init__(self)


    def run(self):
        with threading.Lock():
            StrLengthThread.total_str_length += (len(self.word))
