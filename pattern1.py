a,b,c,d = input().split()
print(a,b,c,d)
n=4
for i in range(0,n):
    for j in range(0,n):
        if j<i:
            print(" ",end="")
        else:
            print("*",end="")
    print("")
