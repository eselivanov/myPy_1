# Ex4-1-List-Comprehension.py

# 1st:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i +1

# -or- same by using list comprehension
[print(x) for x in thislist]

# 2nd:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print( fruits)
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
#print(newlist)
#print("\n")

# -or- the same
newlist = [x for x in fruits if "a" in x]  
print("Has \"a\" in the name: ", newlist)