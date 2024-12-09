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
const i32 MT   = 0;

const char nl  = '\n';


int ipt() {
    int n;
    cin >> n;
    return n;
}

pair<int, int> ivars() {
    int i, v;
    cin >> i >> v;
    return {i, v};
}

void solve() {
    int n = ipt();
    map<long long, int> c;
    set<long long> s;

    for (int _ = 0; _ < n; _++) {
        auto [i, v] = ivars();
        c[i] = v;
        s.insert(i);
    }

    int remainders = 0;

    while (!s.empty()) {
        long long curr = *s.begin();
        s.erase(s.begin());
        int i = 0;

        while (c[curr] > 0) {
            if (c[curr] & 1) {
                if (i == 0) {
                    remainders += 1;
                } else {
                    long long u = curr * (1LL << i);
                    c[u]++;
                    s.insert(u);
                }
            }
            c[curr] >>= 1;
            i++;
        }
    }

    cout << remainders << endl;
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
