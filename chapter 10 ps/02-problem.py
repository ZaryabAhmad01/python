class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"the square of number is {self.n * self.n}")
    def cube(self):
        print(f"the square of number is {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"the square of number is {self.n ** 1/2}")


s=calculator(5)
s.square()
s.cube()
s.squareroot()
