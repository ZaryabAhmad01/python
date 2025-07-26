a = 31

t = type(a) # class int 
print(t)

a = 31.1

t = type(a) # class <float>
print(t)
 
#string 
a = "zaryab"

t = type(a) # class <string>
print(t)

# change the type
a = "3.11" # this is a float because we ""
b = float(a) # a should be change the float
t = type(b)
print(t)
