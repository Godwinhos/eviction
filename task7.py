'''
Online Store Discount
Ask if the user is a registered member.

If yes:

If purchase amount ≥ 100, apply 20% discount.

Else, apply 10% discount.

If no:

If purchase amount ≥ 200, apply 5% discount.

Else, no discount.
'''
#discount = 0
member=   input("is the user a registered member? enter 'yes' or 'no' ")
if member == "yes":
    purchase = float(input("enter your purchase"))
    if purchase >=100:
        discount =20/100
        discount *= purchase
        amount_spent = purchase - discount 
        print(f"your purchase is {purchase} and your discount is {discount}  and your total amount spent is {amount_spent}")
    else:
        discount = 10/100
        discount *= purchase
        print(f"your purchase is {purchase} and your discount is {discount}")
elif member == "no":
    purchase = float(input("enter your purchase"))
    if purchase >= 200:
        discount = 5/100
        discount *= purchase
        print(f"your purchase is {purchase} and your discount is {discount}")
    else:
        print(f"your purchase is {purchase} and no discount")
else:
    print("input 'yes' or 'no'")
