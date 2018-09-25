import math

def combine(input1,input2):
    for item in input2
        if (item<input1[0]):
            input1=item+input1
        elif (item>input1[-1]):
            input1=input1+item
        else:
            for value in input1:
                if


    return input1


def mergesort(array):

    len(array)
    primary=[]
    secondary=[array]
    print(len(secondary))

    while (len(secondary)!=0):
        funct = secondary[0]
        mid = len(funct)//2
        array1 = funct[0:mid]
        array2 = funct[mid:]
        
        if (len(array1) <= 2):
            primary.append(array1)
        else:
            secondary.append(array1)

        print(primary)
        print(secondary)
        
        if (len(array2)<=2):
            primary.append(array2)
        else:
            secondary.append(array2)

        secondary = secondary[1:]

    print("h",primary)

    for i in primary:
        if (len(i)>1):
            if i[0]>i[1]:
                temp0=i[0]
                temp1=i[1]
                i[0]=temp1
                i[1]=temp0

    outputarray=combine(primary)
    return outputarray

mergesort([2,6,1,9,0])



