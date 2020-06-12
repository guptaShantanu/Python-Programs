s=input()
y=int(input())
i=0
k=""
res=[]
while i<len(s):
    k+=s[i]
    if int(k)<y:
        i+=1
    else:
        res.append(k[:len(k)-1])
        print(res)
        k=k[1:]
        
print(res)
        
        
