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


void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(1 << n);
    for (int &x : a) cin >> x;

    vector<int> bigger(a.size(), 0);
    vector<int> res(a.size(), 0);
    vector<vector<int>> prev(a.size(), vector<int>(1));

    for (int i = 0; i < a.size(); ++i) {
        prev[i][0] = a[i];
    }

    for (int i = 0; i < n; ++i) {
        vector<vector<int>> newprev;
        int idx = 0;

        for (int j = 0; j < prev.size() / 2; ++j) {
            vector<int> &merge1 = prev[2*j];
            vector<int> &merge2 = prev[2*j + 1];
            vector<int> new_vec;
            unordered_map<int, int> numsmaller;

            int p1 = 0, p2 = 0;
            while (p1 < merge1.size() && p2 < merge2.size()) {
                if (merge1[p1] > merge2[p2]) {
                    new_vec.push_back(merge2[p2]);
                    numsmaller[merge2[p2]] = new_vec.size();
                    ++p2;
                } else {
                    new_vec.push_back(merge1[p1]);
                    numsmaller[merge1[p1]] = new_vec.size();
                    ++p1;
                }
            }
            while (p1 < merge1.size()) {
                new_vec.push_back(merge1[p1]);
                numsmaller[merge1[p1]] = new_vec.size();
                ++p1;
            }
            while (p2 < merge2.size()) {
                new_vec.push_back(merge2[p2]);
                numsmaller[merge2[p2]] = new_vec.size();
                ++p2;
            }

            newprev.push_back(new_vec);

            for (int _ = 0; _ < new_vec.size(); ++_) {
                bigger[idx] = new_vec.size() - numsmaller[a[idx]];
                if (bigger[idx] <= k && a[idx] >= new_vec.size()) {
                    ++res[idx];
                }
                ++idx;
            }
        }
        prev = move(newprev);
    }

    for (int i = 0; i < res.size(); ++i) {
        cout << res[i] << (i == res.size() - 1 ? '\n' : ' ');
    }
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
