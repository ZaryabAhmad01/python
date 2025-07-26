from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def book(slf,fro, to):
        print(f"ticket number  is:{slf.trainNo} from {fro} To {to}")

    def get_status(slf):
        print(f"Train  is:{slf.trainNo} running on the time")
    
    
    def fare(slf,fro, to):
        print(f"ticket fare in train no is:{slf.trainNo} from{fro} To {to} {randint(222,5555)}")
# Creating a Train object
a = Train(1234)

#callling correct arguments
a.book("multan","rawalpindi")
a.get_status()
a.fare("multan","rawalpindi")