# datetime

from datetime import date, datetime, time 
import time
import types
from typing import Type

# 1- nahveye ijad object
#2- karbordha and vijegiha

dt = datetime(2025, 3, 10, 23,21,30,156489)
print(dt)
dt = datetime.now()
print(dt)
st = "2020/03/02"
# in google: python strptime and click on first result
dt = datetime.strptime(st,"%Y/%m/%d")
print(dt)
dt = datetime.fromtimestamp(time.time()) #tabdil time to datetime
print(dt)
print(type(dt))