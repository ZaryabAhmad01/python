import random #its module
'''
1 for snake 
-1 for water
0 for gun
'''
computer =random.choice([1,-1,0])
youstr=input("Enter your choice: ")
youdict={"s":1, "w":-1, "g":0}
reversedict={1:"snake", -1:"water", 0:"gun"}

you=youdict[youstr]
#we have two 2 number , computer and you

print(f"you chose: {reversedict[you]} \n computer chose: {reversedict[computer]}")

if(computer==you):
    print("draw")

else:
    if((computer - you)==-1 or (computer - you)==2):
        print("you are loos") 
    else:
        print("you are win")





        #we build logic (computer - you) is ka matlab jab jab -1 and 2 a raha hai ham har rahay hai
        
        '''
        if(computer==-1 and you==1): 0
    
        print("you win")
    elif(computer==-1 and you==0):-1
        print("you lose")
    elif(computer==1 and you==-1): 2
        print("you lose")
    elif(computer==1 and you==0):2 1

        print("you win")
    elif(computer==0 and you==1): -1
        print("you lose")
    elif(computer==0 and you==-1):  1
        print("you win")
    else:
        print("something went wrong")

'''