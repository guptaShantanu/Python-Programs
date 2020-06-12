def solve(list1,list2,n):
    resultList=[]
    for i in range(n):
        resultList.append(list2[i]//list1[i])
    minimum=resultList[0]
    for i in range(n):
        if resultList[i]<minimum:
            minimum=resultList[i]
    return minimum
if __name__=="__main__":
    n=int(input())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    result = solve(list1,list2,n)
    print(result)
