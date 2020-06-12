arr=list(map(int,input().split()))
max1=max(arr)
min1=min(arr)
rem=False
color=0
for i in range(min1,max1+1):
    j=0
    while j<len(arr):
        if arr[j]%i==0:
            rem=True
            arr.remove(arr[j])
            j-=1
        j+=1
    if rem==True:
        color+=1
        rem=False
print(color)
        
