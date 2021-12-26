import heapq

n,m=map(int,input().split())
L = tuple(map(int, input().split()))
OL = L
SL = sorted(L)
graph = {SL[0]:[set(),set([SL[1]])],SL[-1]:[set([SL[-2]]),set()]}
for i in range(1,n-1):
    graph[SL[i]]=[set([SL[i-1]]),set([SL[i+1]])]
E = []
#mid = SL[n//2]
#print("mid:"+str(mid))
for _ in range(m):
    u,v = map(int, input().split())
    E.append((u,v))

def get_loss(L):
    loss = 0
    for u,v in E:
        if L[u-1]>L[v-1]:
            loss += L[u-1] - L[v-1]
    return loss

def nxt(L):
    for i in range(n):
        e = L[i]
        for x in graph[e][1]:
            NL = tuple(L[:i]+tuple([x])+L[i+1:])
            yield NL,sum([abs(OL[j]-NL[j]) for j in range(n)])
        for x in graph[e][0]:
            NL = tuple(L[:i]+tuple([x])+L[i+1:])
            yield NL,sum([abs(OL[j]-NL[j]) for j in range(n)])

loss = get_loss(L)
if not loss:
    print(L)
else:
    Q=[(0+loss*0.0,0,L)]
    seen = set([tuple(L)])
    while Q:
        h,step,ss = heapq.heappop(Q)
        for ns,_step in nxt(ss):
            if ns not in seen:
                #print("step="+str(_step))
                #print(' '.join(map(str,ns)))
                seen.add(ns)
                loss = get_loss(ns)
                if not loss:
                    print("step="+str(_step))
                    print(' '.join(map(str,ns)))
                    exit()
                else:
                    heapq.heappush(Q,(_step+loss*0.0,_step,ns))
