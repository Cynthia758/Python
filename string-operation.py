c = "Hello" +" " + "World"
print(c)

print("*"*1)

print("Vaidehi "*5)

print("Hello" == "Vaidehi")

print("Hello" != "World")

print("Mumbai" > "Pune") # Pyton compares with ASCII valuess... for M it is 77 and for P it is 80. So the output will be false.
print("Hello" and "World") # BOth are truthy so returns the second one
print("" and "World")       # → ''  (first is falsy, so it returns it)
print("hello" and "")       # → ''  (second is falsy, so it returns it)
print("" and "") 
# Empty strings are considered to be false.
print(not "hello") # "hello" is truthy so it will return false if it is false then it will return true.
c = "Vaidehi Parmar"
for i in c : 
    print(i)   
print('V' in c)
print('V' not in c)