a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
for i in a:
    print(i)
for i in range(3):
    temp=[]
    for j in range(2,-1,-1):
        temp.append(a[j][i])
    b.append(temp)
print("Rotated")
for i in b:
    print(i)

