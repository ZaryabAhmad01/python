import random
n = random.randint(1,100)

a=-1
Guesses=1

while(a!= n):
    a=int(input(" Guess the number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
    Guesses+=1


print(f"you have guessed the number {n} correctly in {Guesses}")