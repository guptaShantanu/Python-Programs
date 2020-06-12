n,w=input().split()
n=int(n)
w=int(w)

j=1
for i in range(1,int(((n-1)/2))+1):
    print((".|."*j).center(w,"-"))
    j+=2


print('WELCOME'.center(w,'-'))


j-=2
for i in range(1,int(((n-1)/2))+1):
    print((".|."*j).center(w,"-"))
    j-=2
