# Formatting Strings

k = "uid"
v = "sa"
print "%s=******%s" % (k, v)   # evaluates to string 'uid=******sa'

uid = "sa"
pwd = "secret"
print pwd + " is not a good password for " + uid
# -- or --
print "%s is not a good password for %s" % (pwd, uid)

userCount = 6
print "Users connected: %d" % (userCount, )
# but not
#   print "Users connected: " + userCount

print "Today's stock price: %f" % 50.4625     # ..50.462500
print "Today's stock price: %.2f" % 50.4625   # ..50.46
print "Change since yesterday: %+.2f" % -1.5   # ..-1.50
print "Change since yesterday: %+.2f" % 1.5   # ..+1.50
