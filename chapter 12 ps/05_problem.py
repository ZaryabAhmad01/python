n = int(input("Enter a number :"))
table=[n*i for i in range(1,11)] #comprehension 
with open("table.txt","a") as f: # create a file a append 
    f.write(f"Table of {n}{table} \n")  