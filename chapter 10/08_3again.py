class Employee:
    language = "py"
    salary = 5000

    def getinfo(self):
        print(f"the salary is {self.salary} and the language is {self.language}")
    @staticmethod
    def greet():
        print("good mornig")

harry=Employee()
harry.language="js" #intence attribute phaly ata hai
harry.greet()
harry.getinfo()


