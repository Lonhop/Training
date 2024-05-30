n=int(input())
a=[]
mx=-1
c=0
fl=True
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    k=0
    for j in range(n):
        if a[i][j]!=a[j][i] and i!=j:
            fl=False
            break
        else:
            k+=a[i][j]
    if not fl:
        break
    else:
        if mx<k:
            mx=k
            c=i+1
if fl:
    print(c)
else:
    print("NO")
