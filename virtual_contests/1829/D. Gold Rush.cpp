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


void solve(){
    int n, m;
    cin >> n >> m;
    if(n < m)
    {
        cout << "NO" << nl;
        return;
    }
    stack<int> stk;
    unordered_set<int> track;
    stk.push(n);
    while(!stk.empty())
    {
        int curr_val = stk.top();
        stk.pop();
        if(!curr_val) continue;
        if(curr_val == m)
        {
            cout << "YES" << nl;
            return;
        }
        track.insert(curr_val);
        int third = curr_val / 3;
        if(third * 3 != curr_val) continue;
        if(third * 2 >= m && !track.count(third * 2)) stk.push(third * 2);
        if(third >= m && !track.count(third)) stk.push(third);
    }
    cout << "NO" << nl;
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
