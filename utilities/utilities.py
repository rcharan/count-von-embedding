from datetime        import datetime

from progress_bar import ProgressBar
################################################################################
#
# Part 1 : Super Simple Timer
#
################################################################################

# Super simple timer
#  Timing implemented as class methods
#  to avoid having to instantiate
class Timer:

    @classmethod
    def start(cls):
        cls.start_time = datetime.now()

    @classmethod
    def end(cls):
        delta     = datetime.now() - cls.start_time
        sec       = delta.seconds
        ms        = delta.microseconds // 1000
        cls.time  = f'{sec}.{ms}'
        print(f'{sec}.{ms} seconds elapsed')


def lmap(func, iterable):
    return list(map(func, iterable))
