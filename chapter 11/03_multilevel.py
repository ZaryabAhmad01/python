class Employee:
    a=1


class programmer(Employee):
    b=2


class manager(programmer):
    c=3

o=Employee()
print(o.a)
o=programmer()

print(o.a,o.b)#yea ab employe  ka  attribute b shoe karay ga or b yani kay programmer kka b shoe karya ga 

print("hello bro")

o=manager()#yea ab employe  ka  attribute b shoe karay ga or b yani kay programmer kka b shoe kary or manger ka b
print(o.a,o.b,o.c)