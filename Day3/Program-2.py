def pmt(str, step = 0):
	if step == len (str):
		print(''.join(str))
	for i in range(step,len(str)):
		str_cpy = [c for c in str]
		str_cpy[step], str_cpy[i] = str_cpy[i], str_cpy[step]
		pmt(str_cpy, step+1)

s = input("Enter the String:")
print(pmt(s))
