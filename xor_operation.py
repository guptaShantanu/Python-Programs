def solve(arr):
    dict={}
    lis=[]
    new=[]
    for i in range(len(arr)):
        if dict.get(arr[i]):
            d=dict[arr[i]]
            dict[arr[i]]=d+1
        else:
            dict[arr[i]]=1
            lis.append(arr[i])
    for i in range(len(lis)):
        temp_res=-1
        for j in range(i+1,len(lis)):
            temp_res=lis[i]^lis[j]
            if dict[lis[i+1]]%2!=0:
                pass
            else:
                temp_res=0
            if dict[lis[i]]%2!=0:
                pass
            else:
                temp_res=0
            new.append(temp_res)
    res=0
    print(new)
    for i in range(len(new)):
        res=res^new[i]
    return res
            
            
                

if __name__ == "__main__":
    tb=int(input())
    arr = list(map(int,input().split()))
    print(solve(arr))
