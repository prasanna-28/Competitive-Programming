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
    long long l, r, G;
    cin >> l >> r >> G;

    if (G > r) {
        cout << "-1 -1\n";
        return;
    }

    long long M = (l + G - 1) / G;
    long long X = r / G;

    if (M > X) {
        cout << "-1 -1\n";
        return;
    }

    if (M == X) {
        if (M == 1 && G >= l && G <= r) {
            cout << G << " " << G << "\n";
        } else {
            cout << "-1 -1\n";
        }
        return;
    }

    long long best_m = -1;
    long long best_x = -1;
    long long best_diff = -1;

    long long m_low = M;
    long long m_high = min(M + 20LL, X);
    long long x_low = max(X - 20LL, M);
    long long x_high = X;

    for (long long m = m_low; m <= m_high; ++m) {
        for (long long x = x_high; x >= x_low; --x) {
            if (x <= m) {
                break;
            }
            if (__gcd(m, x) == 1) {
                long long diff = x - m;
                if (diff > best_diff) {
                    best_diff = diff;
                    best_m = m;
                    best_x = x;
                } else if (diff == best_diff && m < best_m) {
                    best_m = m;
                    best_x = x;
                }
            }
        }
    }

    if (best_diff == -1) {
        cout << "-1 -1\n";
    } else {
        long long A = G * best_m;
        long long B = G * best_x;
        cout << A << " " << B << "\n";
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
