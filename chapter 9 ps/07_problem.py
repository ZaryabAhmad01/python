with open("lorem435.txt") as f:
    lines=f.readlines()

lineno =1
for line in lines:
     if("zaryab" in line):
          print(f"yes zaryab is present. line No {lineno} ")
          break
     lineno +=1

else:
     print("no zaryab is not present ")