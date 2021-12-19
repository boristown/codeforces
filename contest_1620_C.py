t=int(input())
for _ in range(t):
    n,k,x = list(map(int,input().split()))
    s = input()
    Evt = [] #(a/b,max)
    o,num = '',0
    for i,c in enumerate(s):
        if c != o:
            if o == 'a':
                Evt.append(['a',num,num])
            elif o == '*':
                Evt.append(['b',num*k,0])
            o=c
            num=0
        num+=1
    if o == 'a':
        Evt.append(['a',num,num])
    elif o == '*':
        Evt.append(['b',num*k,0])
    j=len(Evt)-1
    while x>1:
        while Evt[j][0]!='b':
            j-=1
        x2 = (x-1) // (Evt[j][1]+1) + 1
        y2 = (x-1) % (Evt[j][1]+1)
        #print('j='+str(j)+';x2='+str(x2)+';y2='+str(y2))
        Evt[j][2]=y2
        x = x2
        j-=1
    #print(Evt)
    ans = ''
    for a,b,c in Evt:
        ans+=a*c
    print(ans)