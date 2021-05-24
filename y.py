def is_leep_year(year):
	if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
		return True
	else:
		return False
a = int(input('請輸入年:'))
print(is_leep_year(a))