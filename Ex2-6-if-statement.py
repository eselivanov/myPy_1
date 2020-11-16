def fib(n):
    print('n =', n)
    if n > 1:
        return( n * fib(n - 1) )
    else:
        print( 'end of line' )
        return( 1 )
#-----
print("fib(3): ", fib(3))

