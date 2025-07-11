# 1. Print
print("Hello Vaidehi!")
# 2. Input 
input("Enter your age.")
# 3. Type
a = 3
print(type(a))
# 4. Type Conversion
print(int('5'))
print(float('3'))
# 5. Absolute
print(abs(-5))
print(abs(5))
# 6. Power
print(pow(2, 3)) # 2 cube 3
print(pow(2, -4)) # 2 to the power -4
# 7. min/max
print(min([2,1,3,9]))
print(max([2,1,3,9]))
print(min('Vaidehi'))
print(min('vaidehi'))
print(max('Vaidehi'))
print(max('vaidehi'))
# 8. Round
c = 22/7
print(c)
print(round(c))
# 9. Divmod  
# If we enter divmod(a,b) then the output will be (a/b, a%b)
print(divmod(5,2))
# 10. bin/oct/hex
print(bin(4))
print(oct(4))
print(hex(4))
# 11. id
# If I have store any variable and to find out it's address from the memory we use this function
a=3
b=3
print(id(a))
print(id(b))
# For performance reasons, Python reuses objects for small integers (typically from -5 to 256). These are pre-allocated and shared, so any variable assigned a value in this range will point to the same object in memory. So will get the same output
p = 300
q = 300
print(id(p))
print(id(q))
# 12. Ord
# Returns the unicode code point for a one-char string
print(ord('x'))
print(ord('A'))
# 13. Len
# Gives u the length of an iterator 
print(len('Kolkata'))
print(len([1,2,3]))
# 14. Sum
print(sum([1,2,3,4,5]))
# 15. help
help('print')
help('sum')






