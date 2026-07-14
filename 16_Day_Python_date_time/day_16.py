from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

from datetime import datetime
# 当前日期和时间
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("时间:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S 格式
print("时间一:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S 格式
print("时间二:", time_two)

from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import date
d = date(2020, 1, 1)
print(d)
print('当前日期:', d.today())    # 2019-12-05
# 今天的日期对象
today = date.today()
print("当前年份:", today.year)   # 2019
print("当前月份:", today.month) # 12
print("当前日:", today.day)     # 5


from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute 和 second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute 和 second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t22 = timedelta(weeks = 12, days=10, hours=4, minutes=0, seconds=10)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
t33 = t1 - t22
print("t3 =", t3)
print("t33 =", t33)



# Exercises: Day 16
print('\n# 1')
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)


print('\n# 2')
time2 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time2)

print('\n# 3')
string3 = '5 December, 2019'
date3 = datetime.strptime(string3, "%d %B, %Y")
print(date3)


print('\n# 4')
new_year = datetime(year = now.year + 1, month = 1, day = 1)
now = datetime.now()
diff = new_year - now
print(diff)


print('\n# 5')
from datetime import date
time_old = date(year = 1970, month = 1, day = 1)
now = date.today()
diff = now - time_old
print(diff)