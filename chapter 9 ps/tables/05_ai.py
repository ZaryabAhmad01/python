import os

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    # Ensure the directory exists
    os.makedirs("tables", exist_ok=True)
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 2 to 20
for i in range(2, 21):
    generateTable(i)
