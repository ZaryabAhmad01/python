class employee:
    company= "itx"
    name="hello"
    def show(self):
        print(f"the name is {self.name} and companr is {self.company}" )

class coder:
    language="python"
    def printlang(self):
        print(f"ther are many languge but only chosse this languge {self.language}")



class programer(employee,coder):
   company = "zamad"
   def showlang(self):
       print(f"the language is {self.language} and company is {self.company}")


a=employee()
b=programer()


b.show()
b.printlang()
b.showlang()