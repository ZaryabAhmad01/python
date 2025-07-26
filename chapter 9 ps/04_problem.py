word = "donkey"
with open("file.text") as f:
    content=f.read()
    contentnew=content.replace("donkey","####")

    
    with open("file.text","w") as f:
       f.write(contentnew)