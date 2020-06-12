number=int(input())
total_money=int(input())
toys=list(map(int,input().split()))
sorted(toys)
sum=0
count=0
for i in range(len(toys)):
    sum=sum+toys[i]

    if sum>total_money:
        break
    else:
        count+=1

print(count)
        
        
