f=open('14.txt')
c=0
a=f.readline()
r='0123456789ABCDEF'
k=''
q=''
for i in range(len(a)):
    if a[i] in r:
        k+=a[i]
    elif k!='':
        if len(k)>c:
            c=len(k)
            q=k
        k=''
print(c)
print(q)
