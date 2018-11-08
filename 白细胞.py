a,b=[int(x) for x in input().split()]
l=[int(x)for x in input().split()]
l.sort()
c=0
for i in range(len(l)):
    if a>=l[i]:
        c+=1
        a-=l[i]
print(c)
