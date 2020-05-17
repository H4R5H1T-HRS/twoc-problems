#Solution 4
cp = float (input("Enter the cost price of the product: "))
sp = float (input ("Enter the selling print of the product: "))
profit = sp - cp # In case of Profit ATQ
print ("Profit = ",profit)
# To increase the profit by 5% 
new_profit = profit + (profit*.0.5)
new_sp = new_profit + cp 
print ("If we want to increase the print by 5% then the new selling price be ",new_sp)

