from argparse import ArgumentParser
from stopwatch import Stopwatch


def start_timer():
    stopwatch = Stopwatch()
    print("Stopwatch is ready, press 's' to start, 'x' to stop and 'y' to save and exit")
    while True:
        command = input()
        if command == 'y':
            stopwatch.save()
            break
        elif command == 's':
            stopwatch.start()
        elif command == 'x':
            stopwatch.stop()
        else:
            print("Invalid input please press 's' to start, 'x' to stop and 'y' to save and exit")

def parse_args():
    """
    default: Show jobs and total time spent on them
    -job: which job do I want to time (Open up timer, but don't start it)
    -period: show total time spent on a job in given period (date1 - date2)
    -earnings: show total earnings for a given period or session
    -new_job: create a new job

    -job name (-earnings -period)
    -job name

    -period (if job is given display all recorded time, or in specified period)
    -earnings (if job is given display earnings, if not give total for all jobs)

    """
    parser = ArgumentParser(description = "Work session manager, manage projects with a timer and get statistics about time spent")

    parser.add_argument("-n", "--new_job", nargs="2",
    help="Name of a new job you're starting, specify name and hourly rate")

    parser.add_argument("-p", "--period",
    help="The period you want time spent from, date or month is fine")

    parser.add_argument("-e", "--earnings",
    help="The earning you want from given job and or period")

    parser.add_argument("-j", "--job",
    help="The job you want to start recording time for")

    arguments = parser.parse_args()


if __name__ == '__main__':
    parse_args()
