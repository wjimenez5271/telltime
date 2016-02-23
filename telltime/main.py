from datetime import datetime
from time import time
from argparse import ArgumentParser


def epoch_to_datetime(epoch):
    return datetime.fromtimestamp(epoch)

def get_epoch_time():
    return time()

def main():
    parser = ArgumentParser()
    parser.add_argument('epoch_time', type=int, default=-1, nargs='?')
    parser.add_argument('--verbose_format', action='store_true')
    args = parser.parse_args()
    dt = epoch_to_datetime(args.epoch_time)

    if args.epoch_time == -1:
        print "Current epoch time: {}".format(get_epoch_time())
    elif args.verbose_format:
        print dt.strftime("%A %d. %B %Y %I:%M:%S %p" )
    else:
        print dt.isoformat()


if __name__ == '__main__':
    main()