import math
n=50
s=0
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            if a<=b<=c and a+b>c:
                if 2*(a**2)+2*(b**2)>(c**2):
                    m=math.sqrt(2*(a**2)+2*(b**2)-(c**2))/2
                    if m == int(m) :
                        s=s+1
                        print(a,b,c,m)
print(s)

#integral median