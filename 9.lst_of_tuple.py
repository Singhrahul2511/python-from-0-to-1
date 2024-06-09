#if we wish to sort list of tuples or tuples  of list it can be done

import operator
lst = [('Shailesh',24,3455.50),('priyanka',25,5550.32)]
tpl = (['shailesh',24,3455.50],['priyanka',25,5550.32])
print(sorted(lst))
print(sorted(tpl))
print(sorted(lst,key =operator.itemgetter(2)))
print(sorted(tpl,key =operator.itemgetter(2)))