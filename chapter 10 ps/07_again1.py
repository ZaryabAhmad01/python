class programmer:
    company="microsoft"
    def __init__(self,name,salry,pin):
        self.name=name
        self.salary=salry
        self.pin=pin
    

p=programmer("ansari",6000,"washington")
print(p.company,p.salary,p.name,p.pin)

a=programmer("ali",5000,"california")
print(a.company,a.salary,a.name,a.pin)