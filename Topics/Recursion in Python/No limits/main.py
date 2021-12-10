import sys

# Using sys.getrecursionlimit() method
# to find the current recursion limit

# Print the current limit
print(sys.getrecursionlimit())

#change the limit
sys.setrecursionlimit(200)

# Print the new limit
print(sys.getrecursionlimit())
