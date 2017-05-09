import threading, sys



class StrLengthThread(threading.Thread):
    def __init__(self, word):
        self.word = word
        if not isinstance(word, str):
            raise Exception("word is not a string")
        threading.Thread.__init__(self)

    def run(self):
        global total_str_length
        total_str_length = 0;
        with threading.Lock():
            total_str_length = total_str_length + len(self.word)

str_length_threads = []

for word in sys.argv:
    if len(word) == 10:
        total_str_length = 0
    else:
        str_length_thread = StrLengthThread(word)
        str_length_threads += [str_length_thread]
        str_length_thread.start()
for i in str_length_threads:
    i.join()
print "%d" % total_str_length
