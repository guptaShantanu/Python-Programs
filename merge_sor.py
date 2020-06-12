swap=0
def merge(arr,low,mid,high):
    global swap
    swapCount=0
    left=[]
    right=[]
    for i in range(low,mid+1):
        left.append(arr[i])
    for j in range(mid+1,high+1):
        right.append(arr[j])
    i=0
    j=0
    l=len(left)
    r=len(right)
    k=low
    while i<l and j<r:
        if left[i]<right[j]:
            if arr[k]!=left[i]:
                swapCount+=1
            arr[k]=left[i]
            i+=1
            
        else:
            if arr[k]!=right[j]:
                swapCount+=1
            arr[k]=right[j]
            j+=1
        k+=1
    while i<l:
        if arr[k]!=left[i]:
            swapCount+=1
        arr[k]=left[i]
        i+=1
        k+=1
    while j<r:
        if arr[k]!=right[j]:
                swapCount+=1
        arr[k]=right[j]
        j+=1
        k+=1
    swap+=swapCount
    

def merge_sort(arr,low,high):
    if low<high:
        mid = int((high+low)/2)
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
        
arr=[2,5,3,1]
merge_sort(arr,0,len(arr)-1)
print(arr)
print(swap//2)
    
