import time


time_start = 0
time_stop = 0


def start_time():
    global time_start
    time_start = time.time()


def stop_time():
    global time_start
    global time_stop
    time_stop = time.time()
    current_time = time_stop - time_start
    # print(f"Time taken: {current_time * 10 ** 3:.03f}ms")
    return current_time * 10 ** 3


def measure_time():
    temp = stop_time()
    start_time()
    return temp
