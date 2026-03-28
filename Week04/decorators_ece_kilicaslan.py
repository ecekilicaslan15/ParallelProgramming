import time
import tracemalloc

def performance(func):
    def measured_function(*args, **kwargs):
        tracemalloc.start()
        start = time.perf_counter()

        value = func(*args, **kwargs)

        finish = time.perf_counter()
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        measured_function.counter += 1
        measured_function.total_time += finish - start
        measured_function.total_mem += peak_memory

        return value

    measured_function.__name__ = func.__name__
    measured_function.__doc__ = func.__doc__
    measured_function.counter = 0
    measured_function.total_time = 0.0
    measured_function.total_mem = 0

    return measured_function
