n=1000
arr=[False]*(n+1)
p=2
while p*p<=n:
    if arr[p]==False:
        for k in range(p+p,n+1,p):
            arr[k]=True
    p+=1

for i in range(2,n+1):
    if arr[i]==False:
        print(i)
        
        
