class programmer:
    company="microsoft"
    def __init__(self,name,salary,pin): #this object does nor need to call dundur
        self.name= name
        self.salary = salary
        self.pin=pin
    
p = programmer("zaryab", 100000 , 17)
print(p.name,p.company,p.salary,p.pin)

a = programmer("ansari", 200000 , 18)
print(a.name,a.company,a.salary,a.pin)