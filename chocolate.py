def birthday(s, d, m):
    count=0
    if m==1:
        for k in s:
            if k==d:
                count+=1
    for i in range(len(s)-m):
        sum=0
        for j in s[i:i+m]:
            sum=sum+j
        if sum==d:
            count+=1
    return count

print(birthday([2,5 ,1 ,3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1],18,7)
)
