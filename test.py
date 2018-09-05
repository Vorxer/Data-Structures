WinNum=[20,50,80,90,60,85,35,75]
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
        
    
