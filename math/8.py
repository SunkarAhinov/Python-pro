import itertools as it
N=3
l=[]
for i0 in range(1,N+1):
    for i in range(1,N+1):
        l.append(i)
list1 = list(it.combinations_with_replacement(l, N))
list1 = set(list1)
lenlist=[]
sublist = (1, 7, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 2, 5, 5, 5, 5, 5)
s=1
for element in range(len(sublist)-1):
    try:
        if sublist[element] == sublist[element+1]:
            s=s+1
        else :
            lenlist.append(s)
            s=1
        if element == len(sublist)-2:
            lenlist.append(s)
    except:
        continue

    #n sequences