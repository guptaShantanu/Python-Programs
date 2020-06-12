def findSpecialProduct(inputArray):
    lis=[]
    inputArray=list(inputArray)
    mult=1
    for i in range(len(inputArray)):
        mult=mult*inputArray[i]
    print(mult)
    for i in range(len(inputArray)):
        lis.append(mult*pow(inputArray[i],-1))
        print(int(mult*pow(inputArray[i],-1)))
    return lis


findSpecialProduct([3,4,6,7])
