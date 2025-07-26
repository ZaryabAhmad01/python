from functools import reduce

l= [1,25,5,522,444,64,766,356,979,2324]

def greater(a,b):
    if(a>b):
        return a
    return b

r = reduce(greater,l)
print(r)