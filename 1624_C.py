t = int(input())
for i in range(t):
    n = int(input())
    L = list(map(int,input().split()))
    for i in range(n):
        while L[i] > n:
            L[i] = int(L[i] / 2)
    L.sort()
    last = n + 1
    ans = "YES"
    for i in range(n-1,-1,-1):
        while L[i] > last - 1:
            L[i] = int(L[i] / 2)
            L.sort()
        if L[i] < last - 1:
            ans = "NO"
            break
        last-=1
    print(ans)
