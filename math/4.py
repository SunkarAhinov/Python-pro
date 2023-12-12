import math
K=10
X=100
s=0
for k in range(1, K+1):
    for a in range(-X,X+1,1):
        for b in range(-X,X+1,1):
            for c in range(-X,X+1,1):
                if a<b<c:
                    AB = math.sqrt(((a-b)**2)+(((a**2-b**2)/k)**2))
                    BC = math.sqrt(((b-c)**2)+(((b**2-c**2)/k)**2))
                    AC = math.sqrt(((a-c)**2)+(((a**2-c**2)/k)**2))
                    try:
                        angle1=((AB**2+BC**2-AC**2)/(2*AB*BC))*math.sqrt(2)
                        angle2=((AB**2+AC**2-BC**2)/(2*AB*AC))*math.sqrt(2)
                        angle3=((BC**2+AC**2-AB**2)/(2*BC*AC))*math.sqrt(2)
                    except:
                        continue 
                    if 0.999999999999<angle1<1.000000000001 or 0.999999999999<angle2<1.000000000001 or 0.999999999999<angle3<1.000000000001:
                        s=s+1
                        print(angle1, angle2, angle3)
print(s)

#triangle on parabola