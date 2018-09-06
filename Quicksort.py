import math

def Quicksort(inputarray):
    pivot=math.floor((len(inputarray)/2))
    greater=[]
    lesser=[]
    print(pivot)
    for item in inputarray:
        print(inputarray[item - 1])
        if inputarray[item-1]>inputarray[pivot]:
            greater.append(item)
        if inputarray[item-1]<inputarray[pivot]:
            lesser.append(item)
    outputarray=lesser
    outputarray.append((inputarray[pivot]))
    outputarray=outputarray+greater

    print(outputarray)

Quicksort([1,2,3,4,5,6,7,8,9,0])









