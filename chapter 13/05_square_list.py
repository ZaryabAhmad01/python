#MAP EXAMPLE
l=[1,2,3,4,5]

squire=lambda x: x*x
sqlist=map(squire,l)
print(list(sqlist)) 

# Filter example

def even(n):
    if(n%2==0):
        return True
    return False
onlyeven=filter(even,l)  #filter mian function ata hai
print(list(onlyeven))

# Reduce function
#def sum(a,b):
#    return a+b
#print(reduce(sum,l))d