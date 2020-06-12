n=int(input())
prob=[]
for i in range(n):
    prob.append(int(input()))
prob.sort(reverse=True)
start=2
credit=0
for i in range(n//4):
    credit+=prob[start]
    start+=3
print(credit)
    
