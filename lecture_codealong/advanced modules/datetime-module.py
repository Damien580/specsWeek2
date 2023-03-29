import datetime
mytime = datetime.time(13,15,17,999997)
# print(mytime.minute)
# print(mytime.hour)
# print(mytime)

today = datetime.date.today()
# print(today)

# print(today.ctime())

from datetime import datetime
local = datetime(2023, 3, 28, 10,43,22)
# print(local)
local = local.replace(year=2022)
# print(local)

from datetime import date
date1 = date(2022,11,3)
date2 = date(2020,11,3)
result = date1 - date2
# print(result)

datetime1 = datetime(2021, 11,3,22,0)
datetime2 = datetime(2020, 11, 3, 12, 0)
result = datetime1 - datetime2
print(result)
