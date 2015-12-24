# Declaring variables
# note: variable are auto-destroyed when out of scope

if __name__ == "__main__":
    # "\" is a line concatination marker
    myParams = {"server": "mpilgrim", \
                "database": "master", \
                "uid": "sa", \
                "pwd": "secret" \
                }


print myParams

# Assigning Multiple Values at Once
v = ('a', 'b', 'e')
print v

(x, y, z) = v   # x = 'a', y = 'b', z = 'e'
print x, y, z

# Assigning Consecutive Values
print range(7)     # [0, 1, 2, 3, 4, 5, 6]  <-- list
print range.__doc__   # to get usage details of function range

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7) # set tuple values from list
print MONDAY  # 0
print TUESDAY # 1

# multiple variable assignements can be used to for a return tuple