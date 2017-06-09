import numpy as np
def isPalindrome(num):
    #string conversion here maybe?
    #base case
    if len(num) == 0 or len(num) == 1:
	       return True
    #check first and last chars
    if num[0] == num[len(num)-1]:
	       return isPalindrome(num[1:len(num)-1])
    #not a palindrome
    else:
	       return False
a = np.arange(100,1000)
b = a.reshape(900,1)
c = a*b
# a = np.arange(1,10)
# b = a.reshape(9,1)
# c = a*b
highestPal = 0
for row in c:
    for num in row:
        if isPalindrome(str(num)) and num>highestPal:
            print highestPal
            highestPal = num
print highestPal
