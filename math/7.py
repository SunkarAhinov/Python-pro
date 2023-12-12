import math
def func(n):
    l=0
    if n <= 3:
        l=n
    else:
        for i in range(1,math.floor(n/2)+1):
            l = l + 1 +  func(n-2)
    return l
l=[1,1,1,2,3,6,11,23,47,106,235,551,1301,3159]
L=[]
N=10
g=''
for i in range(N):
    g=g+'1'
for i in range(int(g)+1):
    L1=[]
    for j in str(i):
        if j != '0' :
            L1.append(int(j))
    if sum(L1)==N :
            L.append(tuple(sorted(L1)))
L=set(L)
x=0
for a in L:
    s=1
    for b in a:
        s=s*l[b-1]
    x=x+s
print(x)
g=''
for i in range(10):
    g=g+'1'
l=[1,1,1,2,3,6,11,23,47,106,235,551,1301,3159]
L=[]
N=10
g=''
for i in range(N):
    g=g+'1'
for i in range(int(g)+1):
    L1=[]
    for j in str(i):
        if j != '0' :
            L1.append(int(j))
    if sum(L1)==N :
            L.append(tuple(sorted(L1)))
L=set(L)
x=0
for a in L:
    s=1
    for b in a:
        s=s*l[b-1]
    x=x+s
print(x)