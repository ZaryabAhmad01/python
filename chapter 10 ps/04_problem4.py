class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"the square of number is {self.n * self.n}")
    def cube(self):
        print(f"the square of number is {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"the square of number is {self.n ** 1/2}")
         
    @staticmethod  # is nor use self a parameter because we dont need this
    def hello():
        print("Assalam o alaikum there ")


s=calculator(5)
s.hello()
s.square()
s.cube()
s.squareroot()
