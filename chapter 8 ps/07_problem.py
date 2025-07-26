def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
            return n
l =["zaryab", "zainab", "zarnab", "ali", "ab", "hanan"]
print(rem(l,"ab"))