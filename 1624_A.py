import math
t = int(input())
for i in range(t):
    len = int(input())
    L = list(map(int,input().split()))
    ans = max(L)-min(L)
    print(ans)
