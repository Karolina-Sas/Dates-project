# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:12:03 2020

@author: PC
"""
import datetime

def days_in_month(year, month):
   
    first_month = datetime. date(year, month, 1)
    if month == 12: 
        second_month = datetime. date(year+1, 1, 1)
    else:
        second_month = datetime.date(year, month+1, 1)
    num_of_days = second_month - first_month
    return num_of_days.days
print(days_in_month(2020, 1))

def is_valid_date(year, month, day):
    
    if(1 <= year <= 9999) and (1 <= month <= 12) and (0 < day <= days_in_month(year, month)):
        return True
    else:
        return False
 
print(is_valid_date(20000, 1, 0))

def days_between(year1, month1, day1, year2, month2, day2):
  
    first_date = datetime.date(year1, month1, day1)
    second_date = datetime.date(year2, month2, day2)
    difference = second_date - first_date
    if is_valid_date(year1, month1, day1) == False or is_valid_date(year2, month2, day2) == False:
        return 0
    elif first_date > second_date:
        return 0
    else:
        return difference.days
print(days_between(2014, 5, 5, 2014, 5, 6))

def age_in_days(year, month, day):

    current_date = datetime.date.today()
    if is_valid_date(year, month, day) == False:
        return 0
    elif datetime.date(year, month, day) > current_date:
        return 0
    else:
        return days_between(year, month, day, current_date.year, current_date.month, current_date.day)
print(age_in_days(0, 1, 21))



