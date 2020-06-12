line=input()
se={}
i=0
count=0
while i<len(line):
    try:   
        if line[i]=='-':
            if line[i+3]=="-":
                try:
                    d=se[line[i+4:i+8]]
                except:
                    se[line[i+4:i+8]]=1
                    count+=1
                    
                i=i+7
            else:
                try:
                    d=se[line[i+3:i+7]]
                except:
                    se[line[i+3:i+7]]=1
                    count+=1
                i=i+6
    except:
        break
        
            
    i+=1
print(count)
    
