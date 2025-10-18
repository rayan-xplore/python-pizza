print("Welcome to Python Pizza!")
size = input("What size pizza do you want? S, M or L: ").lower()
bill = 0
if size == "s":
    #print("price for your ordered pizza is $15")
    bill += 15
elif size == "m":
    #print("price for your ordered pizza is $20")
    bill += 20
elif size == "l":
    #print("price for your ordered pizza is $25")
    bill += 25
else:
    print("you have typed wrong input")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if pepperoni == "y":
    if size == "s":
        bill+=2
    else:
        bill +=3
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if extra_cheese == "y":
    bill += 1
delivery_charges = input("do you want home delivery? Y OR N: ").lower()
if delivery_charges == "y":
    bill += 10
tip_discount = input("how much will you tip to delivery partner? $2 or $5: ")
if tip_discount == "2":
    bill -= 1
else:
    bill -= 3
print(f"your total bill amount is ${bill}.")