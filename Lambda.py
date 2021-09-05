a = 2  
b = 3

print(lambda a, b: a+b)


################################################

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)



##########################################################

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(4)
print(f(0))

print(f(7))

print(f(70))

################################################

