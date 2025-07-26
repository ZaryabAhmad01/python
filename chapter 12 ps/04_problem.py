try:
   a = int(input("enter a first number:"))
   b = int(input("enter a second number:"))
   print(a/b)
except ZeroDivisionError as z:
   print("infinite") 
