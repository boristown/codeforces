INF = float("Inf")
t=int(input())
for _ in range(t):
    n=int(input())
    mn = INF
    mx = -INF
    mnc = -1
    mxc = -1
    mc = -1
    ans = []
    for _ in range(n):
        l,r,c = map(int,input().split())
        if l < mn:
            mn = l
            mnc = c
            mc = INF
        if r > mx:
            mx = r
            mxc = c
            mc = INF
        if l == mn:
            mnc = min(mnc, c)
        if r == mx:
            mxc = min(mxc, c)
        if l == mn and r == mx:
            mc = min(mc, c)
        ans.append(min(mnc+mxc,mc))
    for a in ans:
        print(a)