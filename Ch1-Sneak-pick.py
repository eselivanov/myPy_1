#Ch1-Sneak-pick.py

# Step 1: representing records
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

print( bob[0], sue[2])
print( bob[0].split()[-1]) # Bob's last name; split() into new list ..
sue[2] *= 1.25
print( sue[2] )

people = [bob, sue]

#for person in people:
#    print(person)

print( people[0][0]) # Bob Smith
print( people[1][0]) # Sue Jones

for person in people:
    person[2] *= 1.20
    print(person[0].split()[-1], person[2])

pays = [person[2] for person in people]
print(pays)         # [36000.0, 48000.0]

pays = map( (lambda x: x[2]), people ) # map is generator
l = list(pays)
print(l)

print( sum( [person[2] for person in people] ) )

people.append(['Tom', 50, 0, None])
print(len( people ))
print(people[-1])
print(people[-1][0])
