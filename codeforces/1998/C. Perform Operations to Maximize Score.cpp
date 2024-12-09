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


void sol() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> z(n);
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> z[i].first;
        a[i] = z[i].first;
    }
    for (int i = 0; i < n; i++) {
        cin >> z[i].second;
    }

    sort(z.begin(), z.end());
    sort(a.begin(), a.end());

    int biggest = -1;
    for (int i = n - 1; i >= 0; i--) {
        if (z[i].second) {
            biggest = i;
            break;
        }
    }

    long long mx = 0;
    if (biggest != -1) {
        vector<pair<int, int>> l = z;
        l.erase(l.begin() + biggest);
        int median = l[(l.size() - 1) / 2].first;
        mx = (long long)a[biggest] + k + median;
        if (biggest == n - 1) {
            cout << mx << endl;
            return;
        }
    }

    auto cond = [&](int x) {
        vector<pair<int, int>> l = z;
        int idx = 0, ops = k;
        for (int i = 0; i < n; i++) {
            if (l[i].first <= x) idx++;
        }
        for (int o = idx - 1; o >= 0; o--) {
            if (ops == 0) break;
            if (l[o].second) {
                int diff = min(x - l[o].first, ops);
                l[o].first += diff;
                ops -= diff;
            }
        }
        sort(l.begin(), l.end());
        return l[(l.size() - 1) / 2].first >= x;
    };

    function<int(int, int, function<bool(int)>)> binsearch = [&](int low, int high, function<bool(int)> cond) {
        while (low < high) {
            int mid = low + (high - low + 1) / 2;
            if (cond(mid)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return cond(low) ? low : z[(z.size() - 1) / 2].first;
    };

    n--;
    pair<int, int> last = z.back();
    z.pop_back();
    long long result = max((long long)last.first + binsearch(a[0], 1e9, cond), mx);
    cout << result << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc;
    if(MT) cin >> tc;
    else tc = 1;
    for (int t = 1; t <= tc; t++) {
        sol();
    }
    cout << endl;
}
