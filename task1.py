def timestamp_to_seconds(year, month, day, hour, minute, second):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_seconds = (year - 1) * 365 * 24 * 60 * 60
    total_seconds += sum(days_in_month[i] * 24 * 60 * 60 for i in range(1, month))
    total_seconds += (day - 1) * 24 * 60 * 60
    total_seconds += hour * 60 * 60
    total_seconds += minute * 60
    total_seconds += second
    return total_seconds


def calculate_time_difference(timestamp1, timestamp2):
    seconds1 = timestamp_to_seconds(*timestamp1)
    seconds2 = timestamp_to_seconds(*timestamp2)
    difference_seconds = seconds2 - seconds1
    return difference_seconds


def seconds_to_days_and_remainder(seconds):
    days = seconds // (24 * 60 * 60)
    remainder_seconds = seconds % (24 * 60 * 60)
    return days, remainder_seconds


date1 = list(map(lambda x: int(x), input().split(' ')))
date2 = list(map(lambda x: int(x), input().split(' ')))
difference_seconds_t = calculate_time_difference(date1, date2)
days_t, remainder_seconds_t = seconds_to_days_and_remainder(difference_seconds_t)
print(days_t, remainder_seconds_t, sep=' ')

# timestamp_1 = (980, 2, 12, 10, 30, 1)
# timestamp_2 = (980, 3, 1, 10, 31, 37)
#
# # Calculate time difference
# difference_seconds_t = calculate_time_difference(timestamp_1, timestamp_2)
#
# # Calculate days and remaining seconds
# days_t, remainder_seconds_t = seconds_to_days_and_remainder(difference_seconds_t)
#
# # Print the results
# print("Number of full days passed:", days_t)
# print("Number of seconds in not-full day:", remainder_seconds_t)
