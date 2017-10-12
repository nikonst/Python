'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
return a string of the form "7:00" indicating when the alarm clock should ring.
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) - '7:00'
alarm_clock(5, False) - '7:00'
alarm_clock(0, False) - '10:00'
'''

def al_clock(day, vacation):
    if vacation == 1:
        if day == 0 or day == 6:
            alarmtime = 'off'
        else:
            alarmtime = '10:00'
    else:
        if day == 0 or day == 6:
            alarmtime = '10:00'
        else:
            alarmtime = '7:00'
    return alarmtime

day = input('Enter the day (0 - Sun, 6 - Sat) > ')
vacation = input('Enter vacation (1 - Yes, 2 - No) > ')
if (day >= 0 and day <=6) and (vacation == 1 or vacation ==2):
    print 'Alarm at ', al_clock(day, vacation)
else:
    print 'Invalid Input'
