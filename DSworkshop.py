import random
import math
from mergesort import *
from QUuicksort import *

def CommonValue(a,b):
    print("a=",a)
    print("b=",b)
    count = 0
    for i in a:
        print(count)
        if a[count] in b:
            count=count+1
    print(count)
    return count



def function1(WinNum,lotto):
    """
        this funcion calculates the total
        number of winners of each class
        1st - 4th class winners
    """
    c1win=0
    c2win=0
    c3win=0
    c4win=0
    reference=int(0)
    numlist=[]
    for index in lotto:
        print(reference,"ref")
        print(lotto[reference])
        numlist=lotto[reference]
        result=CommonValue(numlist,WinNum)
        print("result =",result)
        reference=reference+1
        if (result==6):
            c1win=c1win+1

        elif (result==5):
            c2win=c2win+1

        elif (result==4):
            c3win=c3win+1

        elif (result==3):
            c4win=c4win+1

            
    print("Number of class 1 Wins :",c1win)
    print("Number of class 2 Wins :",c2win)
    print("Number of class 3 Wins :",c3win)
    print("Number of class 4 Wins :",c4win)



def function2(WinNum,lotto):
    """
        interface that allows users to check wining status,
        user enters their id number,
        this function checks weather or not the user wins
    """
    target=int(input("Enter your ID"))
    target=target-1
    count=0
    i=0

    
    numlist = lotto[target]

    print(numlist)
    
    for player in lotto:
        count=CommonValue(numlist,WinNum)


    if (count==6):
        print("You win the game, congratulations!")
    elif (count==5):
        print("You are a 2nd class winner, congratulations!")
    elif (count==4):
        print("You are a 3rd class winner, congratulations!")
    elif (count==3):
        print("You are a 4th class winner, congratulations!")
    elif (count<3):
        print("Thanks for playing lotto. Good luck next time!")

"""Initialisation stage
    generates winning number sequence and store them in an array WinNum[]
    generates all playing numbers lottox[]
    sorts arrays
    wait for user input to perform function 1 or 2"""

"""assume array holding all player numbers"""

    
def main():
    
    WinNum=[]
    for x in range(6):
        rngambiguous = True

        while (rngambiguous == True):    
            rng=random.randint (1, 45)

            if rng in WinNum:
               rngambiguous=True
            else:
                rngambiguous=False
            
        
        WinNum.append(rng);

    print(WinNum)
    """Sort WinNum Insertion sort here"""

    q=0
    for r in (WinNum):
        val=WinNum[q]
        print(q)

        if (val<WinNum[q-1]):
            i=0
            current=WinNum[i]

            while (current < val):
                i=i+1
                current=WinNum[i]

            lower=i
            sub=WinNum[lower:q+1]
            print(sub)
            sub=([sub[-1]] + sub[:-1])
            print(sub)
            x=0

            for y in sub:
                print(lower,x)
                WinNum[lower]=sub[x]
                lower=lower+1
                x=x+1

        print(WinNum)

        q=q+1
        
            
    
    exit=False
    teminput=int(0)
    lotto=[]
    qwer=1

    players = int(input("Enter the number of players"))
    for x in range(players):
        templist=[]
        print("generating",qwer,"/",players)
        qwer=qwer+1
        for i in range(6):
            tempinput =random.randint(1,45)
            templist.append(tempinput);
            """we gon sort some shit here"""
            mid=math.floor(len(templist))
            

            
        lotto.append(templist); 

    progexit=False
    print("HERE:")
    print(lotto[1])

    while (progexit==False):
        print("Enter 1 to chck your score")
        print("Enter 2 to get overall results")
        print("Enter 3 to exit")
        funct=int(input("Awaiting Input"))
        if (funct==1):
            function2(WinNum,lotto)
        if (funct==2):
            function1(WinNum,lotto)
        if (funct==3):
            progexit=True
    
    
main()

    
        
    
    
