s=input()
news=""
i=0
while i<len(s):
    news=news+s[i]*int(s[i+1])
    i+=2
n=int(input())
print(news)
try:
    print(news[n])
except:
    print(-1)
