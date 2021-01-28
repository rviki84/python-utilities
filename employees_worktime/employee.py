# -*- coding: utf-8 -*-
# !/usr/local/bin/python
#
# January 27, 2021, Vignesh Rammohan
#
# Calculation of the employees paid work hours in a week from a timesheet.csv
#


import csv
from datetime import datetime, timedelta


# compute day work hours from start and end time in 09:00-18:00 format
def get_day_hours(times):
    start_end = times.split('-')
    start_time = datetime.strptime(start_end[0], '%H:%M')
    end_time = datetime.strptime(start_end[1], '%H:%M')
    if end_time > start_time:
        time_diff = end_time - start_time
    else:
        time_diff = end_time - start_time + timedelta(days=1)
    day_hrs = time_diff - timedelta(hours=1)  # reduce 1 hour for lunch break which is unpaid
    return day_hrs


class EmployeeWorkHrs:
    """
    Class incorporating the employees paid work hours list calculation,
    a. in whole week
    b. in weekend
    c. those not worked a typical 40 hours a week
    """
    times = []
    emp_week_hours = {}
    emp_weekend_hrs = {}

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        # time sheet as CSV
        with open(self.csv_file, 'r') as csvTS:
            csv_data = csv.DictReader(csvTS)
            for row in csv_data:
                self.times.append(row)

    def get_hours(self, duration="ALL"):
        # compute the total hours either for whole week or for the weekend
        self.read_csv()
        for row in self.times:
            header = [v for k, v in row.items()]
            emp_name = ""
            wk_total_hrs = timedelta(hours=0)
            for index, item in enumerate(header):
                if index == 0:
                    emp_name = item
                elif item:  # if item is not empty
                    if duration == "ALL":  # whole week hours
                        wk_total_hrs += get_day_hours(item)
                    elif duration == "WEEKEND" and index > 5:  # weekend hours
                        wk_total_hrs += get_day_hours(item)

            if duration == "ALL":
                self.emp_week_hours[emp_name] = wk_total_hrs.total_seconds() / 3600
            elif duration == "WEEKEND" and wk_total_hrs.seconds > 0:
                self.emp_weekend_hrs[emp_name] = wk_total_hrs.total_seconds() / 3600

    def print_hours_all(self):
        # print all the dictionaries containing the total hours worked in whole week
        #
        # sort by lastname then first name; but the inner sort does the firstname and this list is used to sort by
        # lastname
        sorted_keys = sorted(sorted(self.emp_week_hours), key=lambda n: n.split()[1])
        self.emp_week_hours = {key: self.emp_week_hours[key] for key in sorted_keys}
        print("\n*** Total paid hours worked in a week ***")
        print(self.emp_week_hours)
        print("\n*** Paid hours not 40 in a week ***")
        week_hours_not_40 = dict((key, self.emp_week_hours[key]) for key in self.emp_week_hours.keys()
                                 if self.emp_week_hours[key] != 40)
        print(week_hours_not_40)

    def print_hours_weekend(self):
        # print the dictionary containing the total hours worked in the weekend
        #
        # sort by lastname then first name; but the inner sort does the firstname and this list is used to sort by
        # lastname
        sorted_keys = sorted(sorted(self.emp_weekend_hrs), key=lambda n: n.split()[1])
        self.emp_weekend_hrs = {key: self.emp_weekend_hrs[key] for key in sorted_keys}
        print("\n*** Total paid hours worked in a weekend ***")
        print(self.emp_weekend_hrs)


# Execute the script/class to calculate employees' different paid hours
emp = EmployeeWorkHrs("timesheet.csv")
emp.get_hours("ALL")
emp.print_hours_all()
emp.get_hours("WEEKEND")
emp.print_hours_weekend()
