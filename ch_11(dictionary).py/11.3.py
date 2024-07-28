#write a prog to sort a dict in asc/des ord by key and asc/dec by value

import operator
d ={'oil':230,'clip':150,'stud':175,'nut':35}
print('Original dict:',d)

#sorted by key
d1 = sorted(d.items())
print('Asc. order by key: ',d1)
d2 = sorted(d.items(),reverse=True)
print('Dec.order by key:',d2)

#sorting by value

d1 =sorted(d.items(),key = operator.itemgetter(1))
print('Asc.order by value:',d1)
d2 = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print('Dec.order by vslue: ',d2)