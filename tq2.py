m=int(input())
count=0
lis=list(map(int,input().split()))
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        for k in range(j+1,len(lis)):
            for l in range(k+1,len(lis)):
                if (lis[i]+lis[j]+lis[k]+lis[l])==m:
                    count+=1
                    print([lis[i],lis[j],lis[k],lis[l]])
print(count)
