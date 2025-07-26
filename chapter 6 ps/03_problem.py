p1 ="lot of money"
p2 ="subscribe this"
p3 ="click this"
p4 ="buy now"
message = input("enter your comment")
if(( p1 in message)or (p2 in message)or (p3 in message)or (p4 in message) ):
    print("this  is spam")
else:
    print("this not spam")