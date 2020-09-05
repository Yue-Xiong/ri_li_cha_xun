year = int (raw_input('year:\n'))
month = int (raw_input('month:\n'))
day = int (raw_input('day:\n'))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if 0<month<=12:
    xuhao = months[month-1]
    xuhao +=day
    leap = 0
    if (year % 4 == 0):
        leap = 1
    days = [31, 28+leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days[month-1]:
       print 'day error!'
    else:
       if (month > 2) and (leap==1):
           xuhao+=1
       print 'it is the %dth day of the year.'  %xuhao
else:
      print 'month error!'
