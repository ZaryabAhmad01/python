class demo:
    a=4

o = demo()
print(o.a) # print class atteibute because intencce attribute is not present
o.a=0  
print(o.a) # intence attribute print intence attribute is present
print(demo.a)#print the class attribute