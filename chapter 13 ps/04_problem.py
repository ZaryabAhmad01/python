def divisible5(n):
    if(n%5==0):
        return True
    return False

a= [1,25,5,522,444,64,766,356,979,2324]

f = list(filter(divisible5,a))
print(f)