from argparse import ArgumentParser
from timer import Timer

def parse_args():
    """
    default: Show jobs and total time spent on them
    -job: which job do I want to time (Open up timer, but don't start it)
    -period: show total time spent on a job in given period (date1 - date2)
    -earnings: show total earnings for a given period or session
    -new_job: create a new job
    """


if __name__ == '__main__':
    parse_args()
    timer = Timer()
    timer.display_timer()
