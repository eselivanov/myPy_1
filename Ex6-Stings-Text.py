# Ex6- Stings and Text 

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x) 
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print( joke_evaluation % hilarious )

w = "This is the left side of ..."
e = "a sting with a right side."

print(w + e)
print("."*14)

formater = "%r %r %r %r"
print( formater % (1, 2, 3, 4) )
print( formater % ("str1", "str2", "str3", "str4"))

print( """
print long 
sting in triple 
quouts
""" )


