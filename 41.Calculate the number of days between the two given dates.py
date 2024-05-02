from datetime import datetime

def days_between_dates(date_str1, date_str2, date_format="%Y-%m-%d"):
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)

    delta = abs(date2 - date1)
    return delta.days

# Example usage:
date_str1 = "2022-01-01"
date_str2 = "2023-01-01"

days_difference = days_between_dates(date_str1, date_str2)
print(f"Number of days between {date_str1} and {date_str2}: {days_difference} days")
