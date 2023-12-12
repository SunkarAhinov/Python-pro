N=int(input())
s=0 
for i in range(int(N**1/2)+1): 
    for j in range(int(N**1/2)+1): 
        if i**2+j**2==N:  
            if i<j:
                print(i,j, end=',') 
                s=s+i 
print()
print(s)
l=[]
for S in range(1,N):
    s=0 
    for i in range(1,int(S**1/2)+1): 
        for j in range(1, int(S**1/2)+1): 
            if i**2+j**2==S:  
                s=s+1
    if s == 0:
            l.append(S)
k4_1=[]
for i in  range(1, int(150/4)):
    s=0
    for j in range(2, i*2+1):
        if (i*4+1)%j==0:
            s=s+1
    if s==0:
        k4_1.append((i*4+1))
    S=0
for i in l:
    for j in k4_1:
        if i % j == 0:
            print(i,end=' ')
            S=S+i
print()
print(S)

#sum of squares done