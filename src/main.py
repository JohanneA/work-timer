from argparse import ArgumentParser
from stopwatch import Stopwatch
from database_manager import Database
from database_manager import Session
from datetime import date


def start_stopwatch():
    stopwatch = Stopwatch()
    print("Stopwatch is ready, press 's' to start, 'x' to stop and 'y' to save and exit")
    while True:
        command = input()
        if command == 'y':
            time = stopwatch.save()
            return time
        elif command == 's':
            stopwatch.start()
        elif command == 'x':
            stopwatch.stop()
        else:
            print("Invalid input please press 's' to start, 'x' to stop and 'y' to save and exit")

def want_to_save():
    print("Do you wan to store this session? y/n ")
    if(input().lower() == 'y'):
        return True
    else:
        print("Session won't be saved")
        return False

def manage_args(args):
    database = Database()
    database.start()

    if args.new_job is not None:
        print(args.new_job)
        database.create_new_job(args.new_job)

    elif args.job is not None and (args.period is None and not args.earnings):
        today = date.today()
        time = start_stopwatch()

        session = Session(args.job, today, time)
        
        if want_to_save():
            database.store_session(session)

    elif args.earnings or args.period is not None:
        print(str(args.earnings) + " " + str(args.period))
        if args.job == None:
            database.get_stats(args.earnings, args.period)
        else:
            database.get_stats(args.job, args.earnings, args.period)
    else:
        print("Something went wrong somewhere")

    database.close()

def define_args():
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

    parser.add_argument("-n", "--new_job",
    nargs=2,
    help="Name of a new job you're starting, specify name and hourly rate")

    parser.add_argument("-p", "--period",
    nargs=2,
    help="The period you want time spent from, date or month is fine")

    parser.add_argument("-e", "--earnings",
    action= "store_true",
    help="The money you've earned from given job and or period")

    parser.add_argument("-j", "--job",
    help="The job you want to start recording time for")

    return parser.parse_args()


if __name__ == '__main__':
    args = define_args()
    manage_args(args)
    #parse arguments
    #if getting info
    #   query result
    #print result
