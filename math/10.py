N = int(input())
N1 = 10**(N+1)-1
T=0
for k in range(19,N1):
    q = str(k)
    l = set()
    for i in range(len(q)-1):
        s=0
        x=0
        for j in range( len(q)-i):
                s = s + int(q[i+j])
                x = x + 1
                if s==10:
                    for k in range(x):
                        l.add((i+k))
                if i+j>len(q):
                    break
    if len(l)==len(q):
        T = T + 1
print(T)

# 10 substring done