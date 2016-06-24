# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


reg_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


def days_in_year_born(y1, m1, d1):
    sum_days = 0
    if is_leap_year(y1):
        while m1 <= 12:
            sum_days += leap_year[m1 - 1]  # need to start from m1-1 because indexing starts from 0, not 1
            m1 += 1  # from month m1 until (including)month 12
    else:
        while m1 <= 12:
            sum_days += reg_year[m1 - 1]  # need to start from m1-1 because indexing starts from 0, not 1
            m1 += 1  # from month m1 until (including)month 12
    return sum_days - d1  # minus the day you were born


def days_in_year_current(y2, m2, d2):
    if is_leap_year(y2):
        return 366 - days_in_year_born(y2, m2, d2)
    else:
        return 365 - days_in_year_born(y2, m2, d2)


def days_between(y1, y2):
    days = 0
    if y1 != y2:
        year_after = y1 + 1
        while year_after <= y2 - 1:
            if is_leap_year(year_after):
                days += 366
                year_after += 1
            else:
                days += 365
                year_after += 1
        return days
    else:
        return days


def days_between_dates(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return days_in_year_born(year1, month1, day1) + days_in_year_current(year2, month2, day2) + days_between(year1, year2)
    else:
        if is_leap_year(year2):
            return days_in_year_born(year1, month1, day1) - 366 + days_in_year_current(year2, month2, day2)
        else:
            return days_in_year_born(year1, month1, day1) - 365 + days_in_year_current(year2, month2, day2)


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
