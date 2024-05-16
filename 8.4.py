#implement queue data structure it's FIFO(first in first out) addition takes place at 
#end and deletion takes place at front

#import collection
import collections
q = collections.deque()

q.append('suhana')
q.append('rahul')
q.append('rohit')
q.append('sohan')
print(q)

#poping from left

print(q.popleft())
print(q.popleft())
print(q)