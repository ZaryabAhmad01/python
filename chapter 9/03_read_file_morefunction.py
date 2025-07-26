
f = open("file.text") # aghr hamy write krna hota to "w "ata read main nhi ata 
#lines= f.readlines()   #yea list main kr deta hai
#print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line3 = f.readline()
# print(line3, type(line3))


# line4 = f.readline()
# print(line4, type(line4))
line=f.readline()
while(line !=""):
    print(line)
    line=f.readline() 

f.close()