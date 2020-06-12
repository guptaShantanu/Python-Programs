elem=list(map(int,input().split()))
even=[]
odd=[]
res=[]
for i in range(len(elem)):
    if elem[i]%2==0:
        even.append(elem[i])
    else:
        odd.append(elem[i])
even=sorted(even)
odd=sorted(odd)
i=len(odd)
j=len(even)
k=0
l=0
while k<i and l<j:
    if len(odd)>len(even):
        res.append(odd[k])
        res.append(even[l])
    else:
        res.append(even[l])
        res.append(odd[k])   
    k+=1
    l+=1
if len(odd)>len(even):
    while k<i:
        res.append(odd[k])
        break
        k+=1
    while l<j:
        res.append(even[l])
        break
        l+=1
else:
    while l<j:
        res.append(even[l])
        break
        l+=1
    while k<i:
        res.append(odd[k])
        break
        k+=1
    
print(res)
    
