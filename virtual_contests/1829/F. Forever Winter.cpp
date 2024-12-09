#include <bits/stdc++.h>

using namespace std;

#define i64 long long
#define i32 int
#define u32 unsigned int
#define u64 unsigned long long

#define len(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const i64 MOD  = 1e9 + 7;
const i64 INF  = 1e9;
const i64 NINF = -(1e9);
const i32 MT   = 1;

const char nl  = '\n';


void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    for(int i = 0; i < m; ++i)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int seen[n + 1];
    for(int i = 0; i <= n; i++) seen[i] = 0;
    for(int i = 0; i < n + 1; i++)
    {
        if(len(adj[i]) == 1)
        {
            seen[adj[i][0]]++;
        }
    }
    int x = 0;
    int y = 0;
    for(int i = 0; i < n + 1; i ++)
    {
        if(seen[i])
        {
            x += 1;
            y = seen[i];
        }
    }
    cout << x << ' ' << y << nl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc;
    if(MT) cin >> tc;
    else tc = 1;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
    cout << endl;
}
