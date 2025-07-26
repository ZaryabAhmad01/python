'''🟠 Question 1: Method Overriding
Create a base class Shape with a method area() that prints "Area of shape".
Create a derived class Rectangle that overrides the area() method to calculate and print the area of a rectangle (length × width).
Write a program to demonstrate method overriding.'''

'''class shape:
    length=12  
    width=10
    area=length+width
    def area1(self):
        print(f"area of the shape is: {self.area}")

class rectangle(shape):
    length=12  
    width=10
    area_of_rec=length*width
    def area_of_rectangle(self):
        print(f"Area of ractengle is {self.area_of_rec}")

a=shape()

a.area1()
b=rectangle()
b.area1()
b.area_of_rectangle()'''# this is correct but not good and  not create logic


class shape:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print(f"the area of the shape is {self.width+self.length}")

class rectangle(shape):
    def area1(self):
        print(f"the area of rantangle is : {self.width*self.length}")

a=shape(12,10)
a.area()
b=rectangle(12,10)
b.area()
b.area1()
    

 