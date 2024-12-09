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
    i64 n, ones, twos, threes;
    ones = INF;
    twos = INF;
    threes = INF;
    int found1, found2, found3;
    found1 = 0;
    found2 = 0;
    found3 = 0;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        i64 size, value;
        cin >> size >> value;
        if(value == 10) twos = min(twos, size);
        if(value == 1) ones = min(ones, size);
        if(value == 11) threes = min(threes, size);
    }

    if((ones < INF && twos < INF) || threes < INF)
    {
        cout << min(ones + twos, threes) << nl;
        return;
    }
    cout << -1 << nl;

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
