costPrice = float(input("Enter the cost price :"))
sellPrice = float(input("Enter the sell price :"))
profit = sellPrice - costPrice
newSellingPrice = 1.05 * profit + costPrice
print("The profit is",profit)
print("New profit would be",newSellingPrice)
