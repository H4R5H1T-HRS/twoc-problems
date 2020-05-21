#Solution 2
num = int (input("Enter the number: "))
a,b = 0,1
print (a,b,end = " ")
i = 2 
while num > i :
	c = a + b
	print (c, end = " ")
 	a = b
 	b = c
 	i += 1