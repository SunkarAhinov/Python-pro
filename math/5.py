import itertools as it
N=10
f=0
for n in range(1,N+1):
    l=[]
    for i in range(n):
        l.append(i)
    list1 = list(it.permutations(l))
    S=0
    for i in list1:
      s=0
      for j in range(n):
        if True:
          try:
            if abs(i[j]-i[j+1])>3:
              s=s+1
          except:
            continue
      if s==0 and i[0]==0 and i[n-1]==n-1:
        S=S+1
    print(n, S)
    f=f+(S**3)
print(f)

import itertools as it
n=10
l=[]
for i in range(n):
    l.append(i)
list1 = list(it.permutations(l))
S=0
for i in list1:
  s=0
  for j in range(n):
    if True:
      try:
        if abs(i[j]-i[j+1])>3:
          s=s+1
      except:
        continue
  if s==0 and i[0]==0 and i[n-1]==n-1:
    S=S+1
print(S)

#jumping frog