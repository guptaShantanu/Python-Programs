# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

dic = defaultdict(list)
lis=[]
n,m=map(int,input().split())
for i in range(n):
    t=input()
    dic[t].append(i+1)
for i in range(m):
    lis.append(input())
for i in range(len(lis)):

    o=dic[lis[i]]
    if len(o)==0:
        print(-1)
    else:
        for k in range(len(dic[lis[i]])):
            print(dic[lis[i]][k],end=" ")
    print("")



