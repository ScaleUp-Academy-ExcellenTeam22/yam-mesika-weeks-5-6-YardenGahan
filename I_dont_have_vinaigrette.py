import random
import time
import datetime

""" 
This program generates a random date between two dates(start,end).
If the date is of a Monday (Monday is 0 in weekday() return value)
The program will print "I don't have Vinaigrette"
(Which I find a little wierd, I mean, who even likes vinaigrette that much?).
"""


def str_time_prop(start, end, time_format, prop):
    """
     This func is taken from GeeksForGeeks and used to turn the date str from user to date object.
     Then it's creating new time object which is the random date we want, and returns it as str.
     @param start: start date from user
     @param end: end date from user
     @param time_format: how the date is presented
     @param prop: random number
     @return: random date in str format
    """
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))
    prop_time = start_time + prop * (end_time - start_time)

    return time.strftime(time_format, time.localtime(prop_time))


def random_date(start, end, prop):
    return time.strftime(str_time_prop(start, end, '%Y-%m-%d', prop))


def get_input_and_generate():
    start_date = input("Enter start date YYYY-MM-DD")
    end_date = input("Enter end date YYYY-MM-DD")

    rand_date = random_date(start_date, end_date, random.random())
    date_list = rand_date.split('-')

    # Send the random date to weekday func which return '0' for Monday
    week_num = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2])).weekday()

    # Check if the date we generated is monday
    if week_num == 0:
        print("אין לי ויניגרט!")

if __name__ == "__main__":
    get_input_and_generate()