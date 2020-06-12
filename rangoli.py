n=int(input())
character=chr(64+n)
width=n+n-1+n-1+n-1
str_wid=3
for i in range(1,n+1):
    if i==1:
        print(character.center(width,'-'))
    else:
        word=""
        jj=0
        for j in range(0,int(str_wid/2)):
            if j==str_wid/2-1:
                word=word+chr(64+n-j)+"-"
               
            else:
                word=word+chr(64+n-j)+"-"
            jj+=1

        jj-=2
        while jj>=0:
            if jj==0:
                word=word+chr(64+n-jj)

            else:
                word=word+chr(64+n-jj)+"-"
                
            
            jj-=1
        print(word.center(width,"-"))
    str_wid+=2

str_wid-=4
for i in range(1,n):
    if i==n-1:
        print(character.center(width,'-'))
    else:
        word=""
        jjj=0
        for j in range(0,int(str_wid/2)):
            if j==str_wid/2-1:
                word=word+chr(64+n-j)+"-"
               
            else:
                word=word+chr(64+n-j)+"-"
            jjj+=1

        jjj-=2
        while jjj>=0:
            if jjj==0:
                word=word+chr(64+n-jjj)

            else:
                word=word+chr(64+n-jjj)+"-"
                
            
            jjj-=1
        print(word.center(width,"-"))
    str_wid-=2
        
        
    
        
                
        
