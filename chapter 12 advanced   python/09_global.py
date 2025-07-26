a=89 #this was global 
def fun():
    global a #global keyword change kar deta hai global variable ko
    a=3
    print(a)

fun()
print(a)