class employee:#parent class
    company="ITC"
    name="gul"
    salary=100000
    def show(self):
        print(f"the name is: {self.name} and the salary is: {self.salary}")


'''class programer:
    company="ITC infotech" 
    def show(self):
        print(f"the name is: {self.name} and the salary is: {self.salary}")
    def showlanguage(self):
        print(f"neme is: {self.name} language is: {self.language}")'''

class programmer(employee):#jo parent class main hai wo to programmer main hai hi
    company="ITC infotech"# its called child class 
    language="python"
    def showlanguage(self):
        print(f"neme is: {self.name} language is: {self.language}")


a=employee()
b = programmer()
print(a.company,b.company)


#b.show()
#b.showlanguage()