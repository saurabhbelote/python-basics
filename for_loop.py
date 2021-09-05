#Only loop the data you want.

people = [{"name": "John", "id": 1}, {"name": "Mike", "id": 4}, {"name": "Sandra", "id": 2}, {"name": "Jennifer", "id": 3}]
for person in filter(lambda i: i["id"] % 2 == 0, people):
    print(person)

{'name': 'Mike', 'id': 4}
{'name': 'Sandra', 'id': 2}


#Sort your data during, not before.

l = [15,6,1,8]
for i in sorted(l):
    print(i)

#We can also do the inverse by setting the reverse parameter to False:
for i in sorted(l,reverse = True):
    print(i)

    


