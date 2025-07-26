class emp:
    a=4
    @classmethod
    def show(cls):
        print(f"class attribute a is : {cls.a}")

e=emp()
e.a=45
e.show()