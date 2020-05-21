num = int (input("Enter the number:"))
for i in range (num):
	x = (str(num-i)+'*')*(num-i)
	print(x[:-1])
for i in range (num):
	y = (str(num-i)+'*')*(i+1)
	print(y[:-1])
