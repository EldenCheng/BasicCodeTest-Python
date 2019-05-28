import time
import datetime

# 无论time与Date中，都有一个strftime方法，作用是格式化输出日期与时间
# %Y  Year with century as a decimal number.
# %m  Month as a decimal number [01,12].
# %d  Day of the month as a decimal number [01,31].
# %H  Hour (24-hour clock) as a decimal number [00,23].
# %M  Minute as a decimal number [00,59].
# %S  Second as a decimal number [00,61].
# %z  Time zone offset from UTC.
# %a  Locale's abbreviated weekday name.
# %A  Locale's full weekday name.
# %b  Locale's abbreviated month name.
# %B  Locale's full month name.
# %c  Locale's appropriate date and time representation.
# %I  Hour (12-hour clock) as a decimal number [01,12].
# %p  Locale's equivalent of either AM or PM

date = time.strftime("%Y-%m-%d", time.localtime())
time = time.strftime("%H:%M:%S", time.localtime())

# 当前日期加n日
nextWeek = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')