f = open("file.text")
f = open("file.text")
f.close()

# same can be writen using with statement like this

with open("file.text")  as f:
    print(f.read())
# you dont have to need to close the file

