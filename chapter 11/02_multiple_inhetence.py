class employee:#parent class 1
    company="ITC"
    name="default  by name is"
    def show(self):
        print(f"the name is: {self.name} and the companay is: {self.company}")
class coder:#parent class number 2
    language = "python"
    def coderlang(self):
        print(f" all languge is best but u chose only:{self.language}")


class programmer(employee,coder):# its called child class
    company="ITC infotech" 
    def showlanguage(self):
        print(f"name is: {self.name} language is: {self.language}")
   

a = employee()
b = programmer()
c = coder()
b.show()
b.showlanguage()
b.coderlang()
