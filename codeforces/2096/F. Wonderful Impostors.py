import sys
from collections import deque
def main():
    input=sys.stdin.readline
    t=int(input())
    out=[]
    for _ in range(t):
        n,m=map(int,input().split())
        z=[]; o=[]
        for i in range(1,m+1):
            x,a,b=map(int,input().split())
            if x: o.append((a-1,b,i))
            else:   z.append((a-1,b,i))
        q=int(input()); qs=[None]*q
        for j in range(q):
            l,r=map(int,input().split()); qs[j]=(l,r,j)
        N=n+1
        par=list(range(N))
        def f(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        # build max‑spanning forest of zero–edges
        lst=[]
        for u,v,i in sorted(z, key=lambda e:e[2], reverse=True):
            ru,rv=f(u),f(v)
            if ru!=rv:
                par[rv]=ru
                lst.append((u,v,i))
        # adjacency of the forest
        head=[-1]*N; to=[]; nxt=[]; w=[]
        for u,v,i in lst:
            nxt.append(head[u]); head[u]=len(to); to.append(v); w.append(i)
            nxt.append(head[v]); head[v]=len(to); to.append(u); w.append(i)
        # LCA + min‑edge on path
        LOG=(N).bit_length()
        up=[[0]*N for _ in range(LOG)]
        mn=[[m+1]*N for _ in range(LOG)]
        depth=[0]*N; seen=[False]*N
        for v in range(N):
            if not seen[v]:
                seen[v]=True; up[0][v]=v; mn[0][v]=m+1; depth[v]=0
                dq=deque([v])
                while dq:
                    u=dq.popleft(); i=head[u]
                    while i!=-1:
                        v2=to[i]
                        if not seen[v2]:
                            seen[v2]=True
                            depth[v2]=depth[u]+1
                            up[0][v2]=u
                            mn[0][v2]=w[i]
                            dq.append(v2)
                        i=nxt[i]
        for k in range(1,LOG):
            pu,pm=up[k-1],mn[k-1]
            cu,cm=up[k],mn[k]
            for v in range(N):
                p=pu[v]
                cu[v]=pu[p]
                x=pm[v]; y=pm[p]
                cm[v]=x if x<y else y
        def getMin(u,v):
            if f(u)!=f(v): return m+1
            r=m+1
            if depth[u]<depth[v]: u,v=v,u
            d=depth[u]-depth[v]; k=0
            while d:
                if d&1:
                    x=mn[k][u]; r=x if x<r else r
                    u=up[k][u]
                d>>=1; k+=1
            if u==v: return r
            for k in range(LOG-1,-1,-1):
                if up[k][u]!=up[k][v]:
                    x=mn[k][u]; r=x if x<r else r
                    x=mn[k][v]; r=x if x<r else r
                    u=up[k][u]; v=up[k][v]
            x=mn[0][u]; r=x if x<r else r
            x=mn[0][v]; r=x if x<r else r
            return r
        # for each type‑1 edge in same comp, record at which L it becomes inconsistent
        ev=[[] for _ in range(m+2)]
        for u,v,i in o:
            if f(u)==f(v):
                j1=getMin(u,v)
                if j1>0:
                    ev[j1].append(i)
        INF=m+1
        best=[INF]*(m+2)
        cur=INF
        for L in range(m,0,-1):
            for i in ev[L]:
                if i<cur: cur=i
            best[L]=cur
        ans=['']*q
        for l,r,j in qs:
            ans[j]='NO' if best[l]<=r else 'YES'
        out.extend(ans)
    sys.stdout.write('\n'.join(out))

if __name__=='__main__':
    main()

