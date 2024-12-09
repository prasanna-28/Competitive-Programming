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
vector<int> sieve(int limit) {
    vector<bool> is_prime(limit + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= limit; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> primes;
    for (int num = 2; num <= limit; num++) {
        if (is_prime[num]) primes.push_back(num);
    }
    return primes;
}

vector<int> primes = sieve(210000);

void sol() {
    int n;
    cin >> n;
    vector<int> colors(n + 1, 0);
    int mx = pow(2, 32 - __builtin_clz(n));
    int col = 0;

    for (int i = 1; i <= n; i++) {
        set<int> mex;
        for (int j : primes) {
            if (j > mx) break;
            int xor_result = i ^ j;
            if (0 < xor_result && xor_result <= n) {
                mex.insert(colors[xor_result]);
            }
        }
        int c = 1;
        while (mex.count(c)) {
            c++;
        }
        col = max(col, c);
        colors[i] = c;
    }

    cout << col << endl;
    for (int i = 1; i <= n; i++) {
        cout << colors[i] << " ";
    }
    cout << endl;
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
