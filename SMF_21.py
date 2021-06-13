"""
Rohan Dalal
20 March 2021
IDT
1st Period
SMF_21
"""
import datetime


# The Date is printed, for example January 22nd, 2020
def print_date():
    date = str(datetime.date.today())
    date_list = date.split('-')
    months_list = ['space', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December']
    year = date_list[0]
    day = date_list[2]
    month = date_list[1].replace('0', '')
    month = months_list[int(month)]
    if (day[-1] == '1'):
        addend = 'st'
    elif (day[-1] == '2'):
        addend = 'nd'
    elif (day[-1] == '3'):
        addend = 'rd'
    else:
        addend = 'th'
    return ('the date is: ' + month + ' ' + day + addend + ', ' + year)
     


def print_time():
    time = datetime.datetime.now()
    time = time.strftime("%X")
    time_list = time.split(":")
    hour = int(time_list[0]) - 4
    minute = time_list[1]
    if (hour > 12):
        print(hour)
        hour = hour-12
        addend = 'PM'
    elif (hour < 12):
        addend = 'AM'
        if (hour == 00):
            hour = 12
    elif (hour == 12):
        addend = 'PM'
    return ('The time is: ' + str(hour) + ':' + minute + ' ' + addend)
    print(time)


def main():
    print(print_date())
    print(print_time())


if (__name__ == '__main__'):
    main()

   
