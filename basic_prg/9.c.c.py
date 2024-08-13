from datetime import date
date1 = (12,6,2002)
date2 =(28,5,2024)
d1 = date(date1[2],date1[1],date1[0])
d2 =date(date2[2],date2[1],date2[0])
days_diff = abs((d2-d1).days)
years_diff = days_diff/365.25
print("days diff",days_diff)
print("years diff",years_diff)