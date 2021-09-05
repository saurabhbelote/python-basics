squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

#insted 

squares = list(map(lambda x: x**2, range(10)))

print(squares)

# or 
squares = [x**2 for x in range(10)]

print(squares)

####################################################

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(combs)

# or

combs = []

for x in [1,2,3]:
    print(x)
    for y in [3,1,4]:
        print(y)
        if x != y:
            combs.append((x, y))

print(combs)


#################################################

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled

a = [x*2 for x in vec]

print(a)

# filter the list to exclude negative numbers
a = [x for x in vec if x >= 0]
print(a)

# apply a function to all the elements
a = [abs(x) for x in vec]
print(a)
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
a = [weapon.strip() for weapon in freshfruit]
print(a)
# create a list of 2-tuples like (number, square)

a = [(x, x**2) for x in range(6)] # error 
print(a)
# the tuple must be parenthesized, otherwise an error is raised
'''
a = [x, x**2 for x in range(6)]
print(a)'''

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
a = [num for elem in vec for num in elem]
print(a)

######################################################

from math import pi
a = [str(round(pi, i)) for i in range(1, 6)]
print(a)

######################################################
