elements=list(map(int,input().split()))
dict={}
lis=[]
for i in range(len(elements)):
    try:
        d=dict[elements[i]]
        dict[elements[i]]=d+1
    except:
        dict[elements[i]]=1
        lis.append(elements[i])
for i in range(len(lis)):
    if dict[lis[i]]>int(len(elements)/2):
        print(lis[i])
        break
else:
    print(-1)
        
        
