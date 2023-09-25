import functools
import time

def timer(func):

    start_time = time.perf_counter()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'You were playing for {end_time - start_time} seconds!')
        return output
    return wrapper