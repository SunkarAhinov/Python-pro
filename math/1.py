import math
def C(n,a,b):
    n1=n
    n2=n
    s1=0
    s2=0
    while(n1>((a+b)/a)):
        s1=s1+1
        n1=n1* (a/(a+b)) -1
    while(n2>((b+a)/b)):
        s2=s2+1
        n2= n2* (b/(a+b))-1
    print(n1,n2,s1,s2)
    x1=math.log(n1 , (a/(a+b)))*(-1)
    x2=math.log(n2 , (b/(a+b)))*(-1)
    s1=s1+x1
    s2=s2+x2
    print(s1,s2)
    s1=s1*b
    s2=s2*a
    if s1>s2:
        return(s1)
    else:
        return(s2)
    

    #guessing game