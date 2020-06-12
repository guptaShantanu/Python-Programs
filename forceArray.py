
def solve(a,b,n,mod):
    arr=[a,b]
    dict={}
    lis=[]
    dict[a]=1
    try:
        d=dict[b]
        dict[b]=d+1
    except:
        dict[b]=1
        lis.append(b)
    for i in range(2,n):
        temp=(arr[i-1]+arr[i-2])%mod
        try:
            d=dict[temp]
            dict[temp]= d+1
        except:
            dict[temp]=1
            lis.append(temp)
        arr.append(temp)
    print(arr)
    result=0
    for i in range(len(lis)):
        result+=dict[lis[i]]**2
    print(result)
        

if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        a,b,n,mod = input().split()
        a=int(a)
        b=int(b)
        n=int(n)
        mod=int(mod)
        solve(a,b,n,mod)
        
