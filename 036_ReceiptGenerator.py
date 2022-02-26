# Receipt Generator for an Indian Market 


print('''
*********** Pooja Kirana Store ************

Instructions:
1. Enter the product name 
2. Enter the quantity 
3. Enter the price of the product 
4. Press 'q' to conclude the purshase.

''')

proList = []
qtyList = []
priceList = []
subTotalList = []
total = 0
subTotal = 0


while True:
    pro = input("\nEnter the Product name: ")    

    if pro == "q":
        print("\nThanks for shopping with us.")
        break

    qty = int(input('Enter the Quantity : '))
    price = float(input('Enter the Price :'))
    subTotal = qty*price 

    proList.append(pro)
    qtyList.append(qty)
    priceList.append(price)
    subTotalList.append(subTotal)

    total += qty * price

print("Product     Quantity        Price       Subtotal")

for i in range(len(proList)):
    print(f"{proList[i]}       {qtyList[i]}         {priceList[i]}           {subTotalList[i]}")

print(f"\nOrder total : {total}")    