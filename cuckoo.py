def cuckoo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return 1*cuckoo(n-1)+2*cuckoo(n-2)+3*1


print(cuckoo(3))
