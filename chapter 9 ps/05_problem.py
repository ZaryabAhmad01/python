
words = ["donkey", "ganda","baigairat"]
with open("file.text", "r") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#" * len(word))


    with open("file.text","w") as f:
       f.write(content)