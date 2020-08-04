def dayOfProgrammer(year, nd_day):
    is_2018 = False
    if year in range(1700, 1918):
        if year % 4 == 0:
            num_of_days_february = 29
        else:
            num_of_days_february = 28
    elif year in range(1919, 2701):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            num_of_days_february = 29
        else:
            num_of_days_february = 28
    else:  # year == 2018, 28 days
        num_of_days_february = 15
        is_2018 = True
    calendar = {1: 31, 2: num_of_days_february, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    sum_of_days = 0
    for month, number_of_days in calendar.items():
        sum_of_days = sum_of_days + number_of_days
        days_over_flow = nd_day - sum_of_days
        if days_over_flow < 0:
            result_month = month
            if is_2018 and month == 2:
                result_day = number_of_days + days_over_flow + num_of_days_february
            else:
                result_day = number_of_days + days_over_flow
            if result_day in range(1, 10):
                result_day_str = '0' + str(result_day)
            else:
                result_day_str = str(result_day)

            if result_month in range(1, 10):
                result_month_str = '0' + str(result_month)
            else:
                result_month_str = str(result_month)
            break
    result = result_day_str + '.' + result_month_str + '.' + str(year)
    return result

if __name__=='__main__':

    result = dayOfProgrammer(2019, 1)
    print(result)
