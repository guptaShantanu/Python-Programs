test=int(input())
for _ in range(test):
	st=input()
	k=int(len(st)/2)
	for i in range(0,k,2):
		print(st[i],end="")
	print("")
