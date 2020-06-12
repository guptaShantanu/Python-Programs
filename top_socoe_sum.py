n=int(input())
k=int(input())
lis=list(map(int,input().split()))
lis=sorted(lis)
n1=len(lis)-1
sum=0
for i in range(k):
    sum+=lis[n1]
    n1-=1
print(sum)
