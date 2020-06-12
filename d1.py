def solve(n):
    result = ""
    data = str(n)
    big = False
    for i in range(len(data)):
        if data[i]=='3' or data[i]=='5':
            continue
        else:
            break
    else:
        for i in range(len(data)-1,-1,-1):
            if data[i]=='3':
                return data[:i]+'5'+'3'*len(data[i+1:])
        else:
            return '3'*(len(data)+1)
    for i in range(len(data)):
        if int(data[i])<3:
            result+='3'
            if int(data[i])<3:
                big = True
        elif int(data[i])==3:
            if big:
                result+='3'
            else:
                result+='5'
        elif int(data[i])<=5:
            if big == False:
                result+='5'
                if int(data[i])<5:
                    big = True
            else:
                result+='3'
        else:
            if big == False:
                result += '33'
                big =True
            else:
                result+='3'
    return result

t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))
