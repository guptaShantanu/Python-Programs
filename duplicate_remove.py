s=input()
dict={}
res=""
for i in range(len(s)):
    try:
        d=dict[s[i]]
    except:
        res+=s[i]
        dict[s[i]]=1
print(res)
