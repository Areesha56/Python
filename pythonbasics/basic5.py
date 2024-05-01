# LOOP Chapter For Loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n,i^2 print.
# Example
# n=3
# The list of non-negative integers that are less than
# 0 1 2 3

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i*i)


if __name__=='__main__':
    n=int(input())
for i in range(n):
    print(i**2)

# Print each fruit in a fruit list:
Fruits=["apple", "banana", "oranges"]
for x in Fruits:
    print(x)

# Loop through the letters in the word "banana":
for y in "pineapples":
    print(y)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
Meats=['Chicken', 'Mutton', 'Fish', 'Beef']
# x means range (number and quantity of things)
for j in Meats:
    if j =='Beef':
        break
    print(j)

Vegetables=['Cabbage', 'Carrot', 'Cucumber', 'Tomato']
for k in Vegetables:
    if k =='Cucumber':
        print(k)
        break
    




       