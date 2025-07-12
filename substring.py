# Accessing Substring from a String
# Concept of Indexing...
c= 'hello'
print(c)
print(c[0])
print('c')
# Types of indexing...
# 1. Positive Index
# The index number which is +ve.
# 2. Negative Index
# you'll move from right to left
print(c[-1])
print(c[-2])

# slicing
c = "Hello World"
print(c[0:4]) # 4 won't be included so the output will be Hell
print(c[2:])
print(c[:3])
print(c[:])
print(c[2:6:2])
print(c[0:6:-1])
# Print(c[start:stop:step])
print(c[::-1])