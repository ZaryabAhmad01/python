class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n + num.n
    
n=number(2)
m=number(4)

print(n + m)# Output: 6




