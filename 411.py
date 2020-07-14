import bs4
import urllib.request as url
import xlwt
from xlwt import Workbook


a="https://411.info/search/?q="
b = "&l=&page="

nameList = []
phoneList = []
addressList = []

# initialize sheet with all headers
wb = Workbook()
mySheet = wb.add_sheet('Sheet 1')
mySheet.write(0,0,'S.No')
mySheet.write(0,1,'Name')
mySheet.write(0,2,'Phone')
mySheet.write(0,3,'Street Address')
mySheet.write(0,4,'Address Locality')
mySheet.write(0,5,'Address Region')
mySheet.write(0,6,'Postal code')

# User input
name = input("Please enter the name")
sheetName = input("Please enter sheet name")
count = 1
count2 = 1
print("\n\t\t::::::::::::::::::::::::::::::::::::::")
print("\t\t:           Jai mahishmati           :")
print("\t\t::::::::::::::::::::::::::::::::::::::\n")
for j in range(30):
    http=url.urlopen(a+name+b+str(j+1))

    first_page = bs4.BeautifulSoup(http, 'lxml')
    divList=[]

    for i in range(10):
        divList.append(first_page.find('div',id="list_item_"+str(count2)))
        print(count2,end=" ")
        count2+=1
    print("")    
    for i in range(len(divList)):
        nameTag = divList[i].find('div',class_="cname")
        phoneTag = divList[i].find('div',class_="phone")
        streetAddressTag = divList[i].find('span',itemprop="streetAddress")
        addressLocalityTag = divList[i].find('span',itemprop="addressLocality")
        addressRegionTag = divList[i].find('abbr',itemprop="addressRegion")
        postalCodeTag = divList[i].find('span',itemprop="postalCode")
        mySheet.write(count,0,count)
        mySheet.write(count,1,"" if nameTag==None else nameTag.text)
        mySheet.write(count,2,"" if phoneTag==None else phoneTag.text)
        ad1 = "" if streetAddressTag == None else streetAddressTag.text
        ad2 = "" if addressLocalityTag == None else addressLocalityTag.text
        ad3 = "" if addressRegionTag == None else addressRegionTag.text
        ad4 = "" if postalCodeTag == None else postalCodeTag.text
        mySheet.write(count,3,ad1)
        mySheet.write(count,4,ad2)
        mySheet.write(count,5,ad3)
        mySheet.write(count,6,ad4)
        count+=1
    print("Page "+str(j+1)+" Completed\n")

wb.save(sheetName+'.xls')
print("\n\t\t::::::::::::::::::::::::::::::::::::::")
print("\t\t:           Work completed           :")
print("\t\t::::::::::::::::::::::::::::::::::::::")


