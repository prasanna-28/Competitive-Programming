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
    int n;
    cin >> n;
    vector<pair<int, int>> edges;

    function<void(int,int)> query = [&](int a, int b) {
        cout << "? " << a << " " << b << endl;
        int x;
        cin >> x;
        if (x == a) {
            edges.push_back({a, b});
        } else if (x != b) {
            query(a, x);
            query(b, x);
        }
    };

    for (int i = 2; i <= n; ++i) {
        query(1, i);
    }

    cout << "!";
    for (const auto& edge : edges) {
        cout << " " << edge.first << " " << edge.second;
    }
    cout << endl;
}

int main() {
    int tc;
    if(MT) cin >> tc;
    else tc = 1;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
    cout << endl;
}
