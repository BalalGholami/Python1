#timedelta

from datetime import datetime, timedelta

d1 = datetime(2025, 3 , 11)
d2 = datetime.now()

duration = d1 - d2 
print(duration.days)
print(duration.total_seconds())
print(type(duration))