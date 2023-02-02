# time

import time

print(time.time())  # time alan


def task():
    for i in range(99000000):
        pass


starttime = time.time()
print("start:   ", starttime)
task()
endtime = time.time()
print("end:     ", endtime)

duration = endtime - starttime

print("duration:", duration)
