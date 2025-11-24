def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
 # Validate inputs
    if year < 1 or month < 1 or month > 12:
        return None
    
    # Days in each month (default February = 28)
    month_lengths = [31, 28, 31, 30, 31, 30, 
                     31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap years
    if month == 2 and is_year_leap(year):
        return 29
    
    return month_lengths[month - 1]

def day_of_year(year, month, day):
#
# Write your new code here.

    if month < 1 or month > 12:
        return None
    
    # Validate day
    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None
    
    # Sum days of previous months
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    return total_days + day

print(day_of_year(2000, 12, 31))
