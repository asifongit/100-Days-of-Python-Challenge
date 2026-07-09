# 10. Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

costprice=int(input("Enter the Cost price==>"))
sellingprice=int(input("Enter the Selling price==>"))

if sellingprice>costprice:
    print("Profit")

elif sellingprice<costprice:
    print("Loss")

else:
    print("No Profit , No Loss")

