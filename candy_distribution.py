candy=int(input())
child=int(input())
lis=[]
for i in range(child):
    lis.append(0)
count=1
i=0
while candy>0:
    if count>candy:
        count=candy
    lis[i]=lis[i]+count
    candy-=count
    i+=1
    if i==child:
        i=0
    count+=1
print(lis)
    
