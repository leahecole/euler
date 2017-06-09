import numpy


n = 0
m = 0
total = 1000
sum = 0
while n<total:
    print n
    sum+=n    
    n+=3
while m<total:
    print m
    if m %3 !=0:
	sum+=m
    m+=5  
print sum 
