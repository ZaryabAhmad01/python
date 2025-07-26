from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro, to):
        print(f"ticket number  is:{self.trainNo} from {fro} To {to}")

    def get_status(self):
        print(f"Train  is:{self.trainNo} running on the time")
    
    
    def fare(self,fro, to):
        print(f"ticket fare in train no is:{self.trainNo} from{fro} To {to} {randint(222,5555)}")
# Creating a Train object
a = Train(1234)

#callling correct arguments
a.book("multan","rawalpindi")
a.get_status()
a.fare("multan","rawalpindi")