#suppose a date is rep as a tuple(d,m,y).prg to create two date find no of days b/w
#2 dates
from datetime import date
d1 =(25,11,2004)
d2 = (25,11,2004)

#cnvrt tuple to date obj.
dt1 =date(d1[2],d1[1],d1[0])
dt2 =date(d2[2],d2[1],d2[0])

#cal diff
diff =abs((dt1-dt2).days)

print(f"no od days b/w {d1} and {d2} is {diff} days. ")