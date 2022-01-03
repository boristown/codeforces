import sys
t=int(input())
for _ in range(t):
    n=int(input())
    print("? 1")
    sys.stdout.flush()
    _ = int(input())
    ans = [0]*n
    M = set(i+1 for i in range(n))
    for i in range(n):
        for m in M:
            print("? " + m)
            sys.stdout.flush()
            tip = int(input())
            tip ,m ,i
            break