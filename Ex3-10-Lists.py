li = ["a", "b", "mpilgrim", "z", "example"]
print("List \"li\"", li)
print("li[0]: ", li[0])
print("li[1]: ", li[1])
print("li[-1]: ", li[-1]) # example
print("li[-2]: ", li[-2]) # z

# it's all about where to start counting from
print( li[-1] == li[len(li) - 1] )

# subset or slice of a lists; note: lists are zero-based
print( li[1:3] )  # returns new list starting from 1st element and up to, but not including 4th element
print( li[:3] )# from beginning to 3rd, not including
print( li[3:] ) # from 3rd to the end
print( li[:] ) # all elements, not the same list though - it's the _new_ one, that happen to have same elements
            # it's also a way to copy lists

li.append("new")
print( li )

li.insert(2, "new")  # note: elements are not unique
print( li )

li.extend(["extend-one", "extend-two"]) # concatenating 2 lists: li and one in the argument of method
print( li )

# Difference between extend and append
li = ['a', 'b', 'c']

li.extend(['d', 'e', 'f'])  # 2 lists were concatendated
print( li, "of", len(li), "elements" )

li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])   # 2nd list added a an element of the 1st one
print( li, "of", len(li), "elements" )


# Searching a List
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
print( li.index("example") )  # get index of the element, 0-based
print( "cccp" in li ) # returns False, as value is not in a list
print( "Example" in li ) # False
print( "example" in li ) # True

# Boolean
print( "Boolean: " )
i = 0
print( i, "=False, ", i == False )  # True

s = ""
print( s, "=False, ", s == False ) # False

l = []
print( l, "=False, ", l == False ) # False

d = {}
print( d, "=False, ", d == False ) # False 

t = ()
print( t, "=False, ", t == False ) # False 

# Removing Elements from a List
i = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
print( li )
li.remove("z")
li.remove("new") # removes 1st occurrence of 'new'
print( li )

print( li.pop() )  # removes last element, returns value of it
print( li )        # new list from original with last element removed
                # .remove() returns None

# List Operators
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']  # almost the same as extend, it concatenates lists, but creates new vs. change old list

print( li )
li += ['two'] # concatenate: li + 'two'
print( li )


li = [1, 2] * 3     # means repeat [1, 2] x3 times, concatenated
                    # same as [1, 2] + [1, 2] + [1, 2]
print( "li = [1, 2] * 3  : ", li, "\n" )

 # Tuple is an immutable list, can not be changed in any way once it is created
 # tuples have no methods, no index, , no add, no remove, no clear etc.
 # but tuples are way faster, whrite-protected compare to lists ,
 # can be use as a key of a dictionary (except for tuple of lists)
 # used on string formating

 # can be converted to list and vice versa - use function tuple

t = ("a", "b", "mpilgrim", "z", "example")
print( t )
print( t[0], t[-1], t[1:3] )
