import random

def game():
    print("You are playing  the game...")
    score=random.randint(1,60)

#fetch the high score 
    with open("highscore.text") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore= int(highscore)
        else:
            highscore=0

    print(f"your score is: {highscore}")
    if(score>highscore):
# write this high score to the file
        with open("highscore.text", "w") as f:
            f.write(str(score))

    return score
game()