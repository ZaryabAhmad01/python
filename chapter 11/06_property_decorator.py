class emp:
    a=4
    @classmethod
    def show(cls):
        print(f"class attribute a is : {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=emp()
e.a=45
e.name="zaryab ahmad"
print(e.fname, e.lname)


#e.show()