import math

def combine(superarray):
    while (len(superarray) != 1):
        temp = superarray[0] + superarray[1]
        temp.sort()
        superarray.pop(0)
        superarray.pop(0)
        superarray.append(temp)
    return superarray[0]


def mergesort(array):

    len(array)
    primary=[]
    secondary=[array]
    print(len(secondary))

    while (len(secondary)!=0):
        funct=secondary[0]
        mid=math.floor(int(len((funct))/2))
        array1=funct[0:mid]
        array2=funct[mid:len(funct)]
        
        if (len(array1)<=2):
            primary.append(array1)
        else:
            secondary.append(array1)

        print(primary)
        print(secondary)
        
        if (len(array2)<=2):
            primary.append(array2)
        else:
            secondary.append(array2)

        secondary.pop(0)

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








