def dup(list):
	out = []
	for i in list:
		if i not in out:
			out.append(i)
	print (out)

list = [1,2,2,3,1]
dup(list)
