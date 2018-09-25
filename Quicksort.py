import math

def Quicksort(inputarray):
    print("Input=",inputarray)
    if (len(inputarray)==1):
        return inputarray
    if (len(inputarray)==0):
        return inputarray
    pivot = inputarray[math.floor((len(inputarray) / 2))]
    greater=[]
    lesser=[]
    print(pivot)
    for item in inputarray:
        print(item)
        if item>pivot:
            greater.append(item)
        if item<pivot:
            lesser.append(item)
        print("Greater=",greater)
        print("lesser=", lesser)
    greater=Quicksort(greater)
    lesser=Quicksort(lesser)
    outputarray=lesser
    print(outputarray)
    outputarray.append(pivot)
    print(outputarray)
    outputarray=outputarray+greater
    print(outputarray)
    return outputarray

print(Quicksort([1,2,3,4,5,6,7,8,9,0]))










