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

int segmentUnionLength(const vector<
                          pair <int,int> > &seg)
{
    int n = seg.size();

    // Create a vector to store starting and ending
    // points
    vector <pair <int, bool> > points(n * 2);
    for (int i = 0; i < n; i++)
    {
        points[i*2]     = make_pair(seg[i].first, false);
        points[i*2 + 1] = make_pair(seg[i].second, true);
    }

    // Sorting all points by point value
    sort(points.begin(), points.end());

    int result = 0; // Initialize result

    // To keep track of counts of
    // current open segments
    // (Starting point is processed,
    // but ending point
    // is not)
    int Counter = 0;

    // Traverse through all points
    for (unsigned i=0; i<n*2; i++)
    {
        // If there are open points, then we add the
        // difference between previous and current point.
        // This is interesting as we don't check whether
        // current point is opening or closing,
        if (Counter)
            result += (points[i].first -
                        points[i-1].first);

        // If this is an ending point, reduce, count of
        // open points.
        (points[i].second)? Counter-- : Counter++;
    }
    return result;
}

vector<int> ilist(int n) {
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        cin >> result[i];
    }
    return result;
}

int binsearch(int low, int high, const function<bool(int)>& condition) {
    int result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (condition(mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}

void solve() {
    int m, n, k, t;
    cin >> m >> n >> k >> t;

    vector<int> a = ilist(m);
    vector<tuple<int, int, int>> arr;

    for (int i = 0; i < k; i++) {
        int l, r, d;
        cin >> l >> r >> d;
        arr.push_back({l, r + 1, d});
    }

    auto cond = [&](int x) {
        vector<pair<int, int>> new_seg;
        for (const auto& [l, r, d] : arr) {
            if (d > x) {
                new_seg.push_back({l, r});
            }
        }
        int s = segmentUnionLength(new_seg);
        return n + 1 + 2 * s <= t;
    };

    int mx = binsearch(0, 2e5 + 1, cond);

    if (mx == -1) {
        cout << 0 << endl;
        return;
    }

    int res = count_if(a.begin(), a.end(), [mx](int i) { return i >= mx; });
    cout << res << endl;
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
