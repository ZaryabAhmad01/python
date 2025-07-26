a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
if(b==0):
    raise ZeroDivisionError("hey our program is nor ment to divide zaro number")
else:
    print(f"The Divion of a/b is = {a/b} ")


