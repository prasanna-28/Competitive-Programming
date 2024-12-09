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
    i32 n;
    cin >> n;
    vector<int> a(n, 0);
    for(int x = 0 ; x < n; x ++)
    {
        cin >> a[x];
    }
    int i = 0;
    int res = 0;
    while(i < n)
    {
        int length = 0;
        while(i < n && !a[i])
        {
            length ++;
            i++;
        }
        i ++;
        res = max(length, res);
    }
    cout << res << nl;

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
