#Solution 1
def isEven(num):
	if (num % 2 == 0):
		print (num, "is Even")
	else:
		print (num, "is Odd")
 

def isPrime(num):
	c = 0
	for i in range(2,num+1):
		if num % i == 0:
			c+=1
	if c == 1 :
		print(num,"is Prime")
	else :
		print (num,"is not Prime")	
	
# Checking number is Palindrome or not using Loop
def isPalindrome(num):	
	pd = 0
	i = 1  
	no = num 
	while (no >= 0):
		rem = no % 10
		no = no // 10
		pd = pd + rem * i  
		i = i * 10
	
	if (num == pd):
		print (num,"is Palindrome")
	else:
		print (num, "in not Palindrome")

# Checking number is Palindroem or not using string silicing
def isPalindrome_str(num): 
	stn = str(num)
	if (stn == stn[::-1]):
		print (num,"is Palindrome")
	else:
		print (num,"is not Palindrome")


def isArmstrong(num):
	stn = str(num)
	arm = 0
	for x in stn:
		a = int(x) ** 3
		arm = arm + a
	if num == arm:
		print (num, "is Armstrong")
	else :
		print (num, "is not Armstrong")
		

num = int (input ("Enter the number: "))
isEven(num)
isPrime(num)
isPalindrome(num)
isPalindrome_str(num)
isArmstong(num)