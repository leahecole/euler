fib = 1
prevfib = 1
newfib = None
sum = 0
while fib <=4000000:
    print "fib " + str( fib )
    if fib % 2 == 0:
	sum += fib 
    temp = fib
    fib = fib + prevfib
    prevfib = temp
   
print "SUM"
print sum 
    
