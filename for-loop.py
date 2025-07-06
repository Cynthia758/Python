# range function
range(1, 11) # 1 will be included, but 11 will not.
list(range(1, 11))

# list(range(1,11,2)) ; here 2 signifinace the difference between the numbers so the outcome will be ...
# [1, 3, 5, 7, 9]

for i in range(1, 11) :
    print(i) # 11 will not be included
print('Another example.')
for  i in range(1,11,2) :
    print(i)
print('Another One...')
for i in range(10,1,-1) :
    print(i)
print('It can also be used like this..')
for i in "Kolkata" :
    print(i)
  