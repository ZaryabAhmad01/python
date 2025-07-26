#how to we check two file content are same
#for file 1

with open("this.txt") as f:
    content1= f.read()

#for file 2
with open("this_copy.txt") as f:
    content2= f.read()

if(content1==content2):
    print("yes these file are identical")
else:
    print("no these file are not identical")



