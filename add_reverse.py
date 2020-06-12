# your code goes here
test=int(input())

for _ in range(test):
	n,m=input().split()
	n=n[::-1]
	m=m[::-1]
	sum=int(n)+int(m)
	sum=str(sum)
	sum=sum[::-1]
	print(int(sum))
