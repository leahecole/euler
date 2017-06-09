import numpy as np
num = 600851475143
# num = 1000
a = np.mat(np.arange(1, num+1))
# b = np.ones((1, num))*num
# c = np.mod(b,a)
# # print a
# # print b
# # print c
# d = np.nonzero(c == 0)
# print a[d]

#check to see if a number is divisibe by a bunch of numbers
def isDivisibleBy(num, mults):
    b = np.ones((1, np.size(mults)))*num
    c = np.mod(b, mults)
    d = np.nonzero(c==0)
    return mults[d]

multiples = []
others = []
def removeMultiples(anArray, multiple):
    b = np.ones((1, np.size(anArray)))*multiple

    c = np.mod(anArray, b)

    d = np.nonzero(c != 0)
    e = anArray[d]
    multiples.append(multiple)
    return e
    # print np.size(anArray)
#Takes too long - next thing to do, go through and remove thngs that are multiples of things
# removeMultiples(a, 10)
i=2
while(i<num):

    if np.size(isDivisibleBy(i, np.mat(multiples)))==0:
        a = removeMultiples(a, i)
    else:
        others.append(i)
    i+=1
    # print np.size(a)
print multiples #THESE ARE PRIME NUMBERS
# print others
# print a
# print np.size(a)
# print np.size(isDivisibleBy(6, np.mat(multiples)))==0

#go through numbers - if
