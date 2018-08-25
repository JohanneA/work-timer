import time
import sys

# for remaining in range(10, 0, -1):
#     sys.stdout.write("\r")
#     sys.stdout.write("{:2d} seconds remaining.".format(remaining))
#     sys.stdout.flush()
#     time.sleep(1)
#
# sys.stdout.write("\rComplete!            \n")

class Time:
    seconds = 0

    def to_hours_and_minutes(self):
        pass

    def to_minutes(self):
        pass


class Timer:
    current_seconds = 0

    def start(self):
        pass

    def stop(self):
        pass

    def save(self):
        time = Time()
        time.seconds = current_seconds
        return time

    def display_timer(self):
        print("Timer is ready, press 's' to start, 'x' to stop and 'y' to save and exit")
        while True:
            command = input()
            if command == 'y':
                #save()
                print("SAVING!")
                sys.exit(0)
            elif command == 's':
                #start()
                print("STARTING!")
            elif command == 'x':
                #stop()
                print("STOPPING!")
            else:
                print("Invalid input please press 's' to start, 'x' to stop and 'y' to save and exit)
