n,m=map(int,input().split())
a=[]
mx=-1
c=0
number=0
mx_1=-1
q=0
r=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j]>mx:
            mx=a[i][j]
            c=i
            number=j
for i in range(n):
    for j in range(m):
        if i!=c or j!=number:
            if a[i][j]>mx_1:
                mx_1=a[i][j]
                q=i
print(mx_1)
print(q)
