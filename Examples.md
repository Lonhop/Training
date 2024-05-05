#Номера телефонов(записаны ли они):

    def f(n):

        a=''

        for i in range(len(n)):

            if n[i].isdigit():

                a+=n[i]

        return a

    n=input()

    s='495'

    q=[]

    if len(f(n))<=7: n=s+str(f(n))

    else: n=f(n)[1:]

    for i in range(3):

        k=input()

        if len(f(k))<=7:

            k=s+f(k)

        else:

            k=f(k)[1:]

        if k==n:

            q.append(1)

        else:

            q.append(0)

    for i in range(3):

        if q[i]:

            print("YES")

        else:

            print("NO")


#Составление наибольшего числа из заданной строки:

    n=input()

    k=''

    for i in range(len(n)):

        if n[i].isdigit():

            k+=n[i]

    k=sorted(list(k))[::-1]

    for i in range(len(k)):

        print(k[i],end='')


#Смещение символов на длину слова(Шифрование):

    def f(s,i):

        k=i

        while i<len(s) and 'a'<=s[k].lower()<='z':

            k+=1

        return k-i

    def slash(l,k):

        if 'a'<=l.lower()<= 'z':

            if 'a'<=l<='z':

                l=chr(ord('a')+((ord(l)+k)-ord('a'))%26)

            else:

                l=chr(ord('A')+((ord(l)+k)-ord('A'))%26)

        return l

    s=input()

    a=[0]*(len(s)+1)

    for i in range(len(s)):

        if 'a'<=s[i].lower()<='z':

            if a[i-1]!=0:

                a[i]=a[i-1]

            else:

                a[i]=f(s,i)

    for i in range(len(s)):

        print(splash(s[i],a[i]),end='')

#Маски сети(можжно ли из шаблона сделать маску) 

1 способ:

    s=input()

    for p in range(5):

        a=input()

        n=1

        q=0

        i=0

        f=1

        while q<len(s) and i < len(a) and f and n:

            if s[q]=='?':

                i+=1

                q+=1

            elif s[q]=='*':

                n=0

            else:

                if s[q]!=a[i]:

                    f=0

                i+=1

                q+=1


        if n==0:

            for w in range(-1,-len(s)-q,-1):

                if s[w]!=a[w] and s[w]!='?':

                    f=0

                    break

        if f==0:

            print('NO')

        elif '*' not in s and len(a)!=len(s):

            print('NO')

        else:

            print('YES')

2 способ:

    import random

    import re

    m=input()

    pat='^'+m.replace('.',' ').replace('?','.').replace('*','.*').replace(' ', '\.')+'$'

    while True:

        try:

            s=input()

        except:

            break

        if re.fullmatch(pat,s):

            print('YES')

        else:

            print('NO')


