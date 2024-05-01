 # The continue Statement
        # With the continue statement we can stop the current iteration, and continue with the next:

        # Print all numbers from 0 to 10, except 4:
for x in range(10):
    if x == 4 :
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example
# Print all numbers from 0 to 9:
for x in range(10):
    print(x)

# Example
# Print all even numbers from 0 to 10:
for x in range(10):
    if x % 2 == 0:
        print(x)

# Example
# Print all odd numbers from 0 to 10:
for x in range(10):
    if x % 2 != 0:
        print(x)    

for x in range(2,30,30):
    print(x)