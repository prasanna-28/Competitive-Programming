#include <bits/stdc++.h>
using namespace std;

#define i64 long long

vector<i64> build_pair_diff_array(const vector<i64>& arr) {
    int n = arr.size();
    int maxPairs = n / 2;
    vector<i64> D(maxPairs + 1, 0);
    for (int i = 1; i <= maxPairs; ++i) {
        D[i] = D[i-1] + (arr[n - i] - arr[i - 1]);
    }
    return D;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while(t--) {
        int n, m;
        cin >> n >> m;

        vector<i64> A(n), B(m);
        for(int i = 0; i < n; ++i) cin >> A[i];
        for(int j = 0; j < m; ++j) cin >> B[j];

        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        auto DA = build_pair_diff_array(A);
        auto DB = build_pair_diff_array(B);
        int maxPairsA = n / 2;
        int maxPairsB = m / 2;

        i64 kmax = min({ (long long)(n + m) / 3, (long long)n, (long long)m });
        cout << kmax << "\n";
        if(kmax == 0) continue;

        vector<i64> ans(kmax + 1, 0);

        for (int k = 1; k <= kmax; ++k) {
            int p_min = max({0, 2*k - m, k - maxPairsB});
            int p_max = min({k, n - k, maxPairsA});

            if(p_min > p_max) {
                ans[k] = 0;
                continue;
            }

            int L = p_min;
            int R = p_max;
            while(R - L >= 3) {
                int m1 = L + (R - L) / 3;
                int m2 = R - (R - L) / 3;
                int q1 = k - m1;
                int q2 = k - m2;
                i64 val1 = DA[m1] + DB[q1];
                i64 val2 = DA[m2] + DB[q2];
                if(val1 < val2) {
                    L = m1 + 1;
                } else {
                    R = m2 - 1;
                }
            }
            i64 best = 0;
            for(int p = L; p <= R; ++p) {
                int q = k - p;
                if(p >= 0 && q >= 0 && p <= maxPairsA && q <= maxPairsB) {
                    i64 candidate = DA[p] + DB[q];
                    if(candidate > best) best = candidate;
                }
            }
            ans[k] = best;
        }

        for (int i = 1; i <= kmax; ++i) {
            cout << ans[i] << (i < kmax ? ' ' : '\n');
        }
    }
    cout << endl;

    return 0;
}

