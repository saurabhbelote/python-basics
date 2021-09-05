fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4) ) # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop() # to remove last items
print(fruits)

fruits.copy()  #copy of the list.
print(fruits)


fruits.extend('kings')
print(fruits)


###########################################################################

#Using Lists as Stacks

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()

print(stack)

stack.pop()

stack.pop()

print(stack)


################################################################

#Using Lists as Queues

from collections import deque


queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves

print(queue.popleft())                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival