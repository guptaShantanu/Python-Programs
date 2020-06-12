import csv

a=["a","b","c"]
b=["q","w","r"]


with open("data.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(a)
    writer.writerow(b)
    file.close()



with open("data.csv","r") as file:
    reader=csv.reader(file)
    for item in reader:
        print(item)
