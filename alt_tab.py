process=int(input())
tab=int(input())
pro_list=list(map(int,input().split()))
if tab==1 and tab=0:
    print(pro_list)
tab=tab%process
if tab==0:
    tab=process
delete=pro_list[tab-1]
pro_list.remove(delete)
pro_list.insert(0,delete)
print(pro_list)
