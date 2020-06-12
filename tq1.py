def getSum(n):
    sum=0
    while n!=0:
        d=n%10
        sum+=d
        n=n//10
    return sum

row=int(input())
col=int(input())
matrix=[]
flag=0
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(int(input()))
    matrix.append(temp)
for i in range(row-1):
    for j in range(col-1):
        lis=[]

        for k in matrix[i][j:j+2]:
            lis.append(k)
        for k in matrix[i+1][j:j+2]:
            lis.append(k)
        for k in range(len(lis)):
            if lis[k]%getSum(lis[k])==0:
                pass
            else:
                break
        else:
            flag+=1
            print("-------- "+"GOOD MATRIX "+str(flag)+" ---------")
            print(matrix[i][j:j+2])
            print(matrix[i+1][j:j+2])
            print("============================\n")
print("Total good matrix = "+str(flag))
            
            
