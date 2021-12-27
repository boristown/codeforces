t=int(input())
for _ in range(t):
    n = int(input())
    P = list(map(int,input().split()))
    s = input()
    llike = []
    ldislike = []
    for i,c in enumerate(s):
        if c == '1':
            llike.append((P[i],i))
        else:
            ldislike.append((P[i],i))
    llike.sort()
    ldislike.sort()
    nlike = len(llike)
    ndislike = len(ldislike)
    arrlike = [ndislike+1+i for i in range(nlike)]
    arrdislike = [1+i for i in range(ndislike)]
    ans = [0]*n
    for i,e in enumerate(llike):
        _,j=e
        ans[j] = str(arrlike[i])
    for i,e in enumerate(ldislike):
        _,j=e
        ans[j] = str(arrdislike[i])
    print(" ".join(ans))
    
