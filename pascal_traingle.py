#upper pyramid
n=int(input())
for i in range(1,n+1):
    print((("*"*i).center(n,' ')).ljust(i%2,' '))
