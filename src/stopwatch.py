import time
import threading
import sys


def counter(stopwatch):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds passed.".format(stopwatch.current_time))
        sys.stdout.flush()
        time.sleep(1)
        stopwatch.current_time += 1


class Time:
    seconds = 0

    def to_hours_and_minutes(self):
        pass

    def to_minutes(self):
        pass


class Stopwatch:
    def __init__(self):
        self.isRunning = False
        self.current_time = 0
        self.clock = threading.Thread(target=counter, args=(self,))

    def start(self):
        print("STARTING!")
        self.clock.start()
        self.isRunning = True

    def stop(self):
        print("STOPPING!")
        self.isRunning = False

    def save(self):
        print("SAVING!")
        print (self.current_time)
        self.isRunning = False
        self.clock.do_run = False
        return self.current_time
