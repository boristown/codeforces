import math

def eval(mid,n,arr,nmin,nsum,k,ngap):
    nmin2 = nmin-mid
    nsum -= mid
    if nsum <= k:
        return mid
    ans = mid
    for i in range(n-1):
        nele = arr[i]
        ngap = nele - nmin2
        nsum -= ngap
        ans += 1
        if nsum <= k:
            return ans
    return ans + nsum - k

t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    nsum = sum(arr)
    if nsum <= k:
        print("0")
    else:
        arr.sort(reverse=True)
        nmin = arr[-1]
        ngap = nsum - k
        nmax = nmin * n
        l,r=0,ngap
        #if nmax > k:
        #    l = math.ceil((nmax - k)/float(n))
        ans = r
        while l <= r:
            mid1,mid2 = (l*2+r)//3,(l+r*2)//3
            ev1,ev2 = eval(mid1,n,arr,nmin,nsum,k,ngap),eval(mid2,n,arr,nmin,nsum,k,ngap)
            ans = min(ans,ev1,ev2)
            if ev1 == ev2:
                l = mid1+1
                r = mid2-1
            elif ev1 > ev2:
                l = mid1 + 1
            else:
                r = mid2 - 1
        print(ans)