import math

def combine(superarray):
    loopcontrol=len(superarray)
    print(loopcontrol)
    iterate=0
    outputar=[]
    for item in superarray:
        temparray=[]
        for x in range(2):
            subarray=superarray[0]
            superarray.pop(0)
            temparray=temparray+subarray
        temparray.sort()
        print(temparray)
        outputar=outputar+temparray
        iterate=iterate+2
        if (len(superarray)<iterate):
            print("wut")
            
    print(outputar)

        
'''    

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

    primary[]


     
    
    print(primary)
    final=[]


            
    
    

    
    
mergesort([45,43,76,13,90,80,78])
'''

combine([[2,4,9],[8,7,1],[3,6,8]])

