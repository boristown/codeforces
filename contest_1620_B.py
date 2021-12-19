n=int(input())
for i in range(n):
    w,h = list(map(int,input().split()))
    top = list(map(int,input().split()))
    bottom = list(map(int,input().split()))
    left = list(map(int,input().split()))
    right = list(map(int,input().split()))
    mx1 = top[-1] - top[1]
    mx2 = bottom[-1] - bottom[1]
    mx3 = left[-1] - left[1]
    mx4 = right[-1] - right[1]
    ans1 = max(mx1,mx2)*h
    ans2 = max(mx3,mx4)*w
    print(max(ans1,ans2))