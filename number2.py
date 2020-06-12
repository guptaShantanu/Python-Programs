def power(n,k):
    return 2**k
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
total_pair+=power(2,pos_count)

if neg_count>0:
    total_pair*=power(2,neg_count-1)
    print(total_pair)
