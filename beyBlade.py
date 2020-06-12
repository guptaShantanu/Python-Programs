def solve(myTeam,opponent,n):
    start=0
    winCount=0
    myTeam.sort(reverse=True)
    opponent.sort(reverse=True)
    for i in range(n):
        for j in range(start,n):
            if myTeam[i]>opponent[j]:
                winCount+=1
                start=j+1
                break
            if j==n-1:
                return winCount
    return winCount
    
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        myTeam = list(map(int,input().split()))
        opponent = list(map(int,input().split()))
        print(solve(myTeam,opponent,n))
        
    
