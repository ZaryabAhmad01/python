class Employee:
    def __init__(self):
        print("constructure of employee")
    a=1


class programmer(Employee):
    def __init__(self):
        super().__init__()
        print("constructure of programmer")
    b=2
    
    
class manager(programmer):
    def __init__(self):
        print("constructure of manager")
    c=3

# o=Employee()
# print(o.a)

o=programmer()
print(o.a,o.b)

print("hello bro")

# o=manager()
# print(o.a,o.b,o.c)