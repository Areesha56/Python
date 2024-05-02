# we use this module of python which unpacks the array into individual elements.
import __future__
import sys

# n=int(input())
# arr = [i for i in range(n)]
# print(*arr, sep=' ', end='\n')

# var1, var2, var3=1,2,3
# print(var1, var2, var3)
# sep: defines the delimiter between the values.
# end: defines what to print after the values.
# file defines the output stream.
# First Solution

n=int(input())
arr=[i+1 for i in range (n)]
print(*arr, sep='', end='\n',file=sys.stdout)

# Second Solution
n = int(input())
arr = list(range(1, n+1))
print(*arr, sep='', end='\n')


r=int(input())
arr=list(range (12, r+1))
print(*arr, sep='', end='\n')