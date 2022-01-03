import math
t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    m = math.ceil(n/2.0)
    if m < k:
        print("-1")
    else:
        for i in range(n):
            line = ""
            for j in range(n):
                if i == j and i%2 == 0 and k > 0:
                    line+='R'
                    k-=1
                else:
                    line+='.'
            print(line)
    