n=int(input())
m=int(input())
dept=[]
for i in range(n):
    temp = list(map(int,input().split()))
    dept.append(temp)
i=0
connection=0
ladyCount1=0
ladyCount2 = 0
while i<n:
    for k in range(m):
        ladyCount2+=dept[i][k]
    if ladyCount2==0:
        pass
    else:
        connection+=ladyCount2*ladyCount1
        ladyCount1=ladyCount2
        ladyCount2=0
    i+=1
print(connection)
            
    
    
