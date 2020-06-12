line=input().split(" ")
word=""
for i in line:
    if i[0].isalpha()==False:
        word=word+i+" "
    else:
        word=word+i.title()+" "
if word[:len(word)-1]=="Q W E R T Y U I O P A S D F G H J K L Z X C V B N M Q W E R T Y U I O P A S D F G H J K L Z X C V B N M":
    print(True)
else:
    print(False)
