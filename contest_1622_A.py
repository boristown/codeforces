t=int(input())
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    if a==b and c%2==0 or b==c and a%2==0 or a==c and b%2==0:
        print("YES")
    elif a+b == c or b+c == a or a+c==b:
        print("YES")
    else:
        print("NO")
