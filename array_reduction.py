
def solve(n,arr):
    combination=1
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        temp_sum=arr[i]+arr[i+1]
        if arr[i]*2>=arr[i+1] and arr[i+1]*2>=arr[i]:
            combination*=2
        arr[i+1]=temp_sum
    return combination

        

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
    
    
