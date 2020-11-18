# Ex10-Escape.py
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print( tabby_cat )
print( persian_cat )
print( backslash_cat )
print( fat_cat )

c = 0
while c < 5 : # True:
  for i in ["/","- ","|","\\","|"]:
    c += 1
    print( "%s\r" % i, )
