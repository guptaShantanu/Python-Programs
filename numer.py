def fact(n):
    if n==1:
        return 1
    if n==0:
        return 1
    return n*fact(n-1)
arr=list(map(int,input().split()))
neg_count=0
zero_count=0
pos_count=0
total_pair=0

for i in range(len(arr)):
    if arr[i]<0:
        neg_count+=1
    elif arr[i]>0:
        pos_count+=1
    else:
        zero_count+=1
pos=0
for i in range(1,pos_count+1):
    pos+=int(fact(pos_count)/(fact(pos_count-i)*fact(i)))
if neg_count>=1:
    for i in range(1,neg_count+1,2):
        total_pair+=int(fact(neg_count)/(fact(neg_count-i)*fact(i)))*pos
    
else:
    print(total_pair)

print(total_pair+neg_count)
    
    
