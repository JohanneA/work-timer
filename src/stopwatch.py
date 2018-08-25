import time
import threading
import sys


def counter(stopwatch):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        if stopwatch.is_running:
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds passed.".format(stopwatch.current_time))
            sys.stdout.flush()
            time.sleep(1)
            stopwatch.current_time += 1
        else:
            time.sleep(1)


class Stopwatch:
    def __init__(self):
        self.is_running = False
        self.current_time = 0
        self.clock = threading.Thread(target=counter, args=(self,))

    def start(self):
        self.is_running = True
        if not self.clock.is_alive():
            self.clock.start()

    def stop(self):
        self.is_running = False

    def save(self):
        print (self.current_time)
        self.is_running = False
        self.clock.do_run = False
        return self.current_time
