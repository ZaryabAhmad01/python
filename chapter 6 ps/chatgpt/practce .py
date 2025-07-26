bill= int(input("enter your amount: "))
if(bill>=5000):
    discount = bill*0.20
    final_bill= bill-discount
    print("you get 20% discount")
    print(final_bill)
  
elif(bill>2000 and bill<5000):
    discount = bill*0.10
    final_bill= bill-discount
    print("you get 10% discount")
    print(final_bill)

else:
    print("sorry no discount")
    print(bill)
