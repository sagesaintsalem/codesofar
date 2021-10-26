def is_year_leap(year):
    if (year % 4 == 0) and (year % 400 == 0):
        return True
    elif (year % 4 == 0)and (year % 100 != 0):
        return True
    else:
        return False

def days_in_month(year, month):
    is_year_leap(year)
    if month == 2 and is_year_leap(year):
        return 29
    elif month == 2:
        return 28
    elif month == 9 or month == 4 or month == 6 or month == 11:
        return 30
    elif type(month) is str or type(year) is str:
        return None
    else:
        return 31
        
#Test code was written by Cisco, but updated by me to include testing for string input.

test_years = [1936, 1990, 2016, 1987]
test_months = [2, 2, "jan", 9]
test_results = [29, 28, None, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
