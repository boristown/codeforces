t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    #a+c=2*b
    ans = "NO"
    a2 = b*2-c
    if a2 >= a and a2 % a == 0:
        ans = "YES"
    c2 = b*2-a
    if c2 >= c and c2 % c == 0:
        ans = "YES"
    b4 = a+c
    if b4 % 2 == 0:
        b2 = b4 / 2
        if b2 >= b and b2 % b == 0:
            ans = "YES"
    print(ans)
