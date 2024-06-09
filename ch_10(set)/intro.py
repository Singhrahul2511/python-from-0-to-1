#set is like a list with exception that it does not contains duplicates values
#generally set is like list and it is mutable.their content can be changed

s = {'gate','fate','late'}
s.add('rate')
print(s)
#but if you wnat to make it as a immutable then you need to use frozenset

s =frozenset({'gate','fate','late'})
s.add('rate')#it will show error because we have used frozenset to make it immutable.

#llry we can convert a list into set()

lst = [23,45,67,76]
s = set(lst)
print(s)