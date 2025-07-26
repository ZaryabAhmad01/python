class complex:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def __add__(self,c2):
        return complex(self.i + c2.i , self.j + c2.j)
    
    def __str__(self):
        return f"{self.i}+{self.j}j"
        
c1=complex(1,3)
c2=complex(2,4)

print(c1 + c2)
