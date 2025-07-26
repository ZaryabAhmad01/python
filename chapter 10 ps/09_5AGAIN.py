from random import randint
class train:
    def __init__(self,TRAINno):
        self.TRAINno=TRAINno
    def bookticket(self,fro,to):
        print(f"ticket is book train no is {self.TRAINno} from {fro} and to {to} ")
    def get(self,):
          print(f"train is running on time {self.TRAINno}")

    def getfare(self,fro,to):
     print(f"ticket is book train no is {self.TRAINno} from {fro} and to {to}  {randint(222,555)}")

t=train(363610)
t.bookticket("multan","lahore")
t.get()
t.getfare("multan","lahore")