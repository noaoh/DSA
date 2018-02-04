# Based on https://zapier.com/engineering/profiling-python-boss/
import time

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("{0} took {1} seconds".format(f.__name__, end - start))
        return result
    return f_timer
