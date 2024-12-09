#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MOD = 998244353;

const int MAX = 3000;

ll fact[MAX + 1], inv_fact[MAX + 1];

ll power_pow(ll a, ll b, ll mod){
    ll res = 1;
    a %= mod;
    while(b > 0){
        if(b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>=1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    fact[0] = 1;
    for(int i = 1; i <= MAX; i++){
        fact[i] = fact[i-1] * i % MOD;
    }

    inv_fact[MAX] = power_pow(fact[MAX], MOD-2, MOD);
    for(int i = MAX-1; i >= 0; i--){
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD;
    }

    auto comb = [&](int x, int y) -> ll {
        if(x < y) return 0;
        return fact[x] * inv_fact[x - y] % MOD * inv_fact[y] % MOD;
    };

    int n, m;
    cin >> n >> m;

    vector<int> arr(n);
    for(auto &x : arr) cin >> x;
    sort(arr.begin(), arr.end(), greater<int>());

    vector<vector<ll>> dp(n+1, vector<ll>(m+1, 0));
    dp[0][0] = 1;

    vector<ll> res(n+1, 0);

    for(int i = 0; i < n; i++){
        ll total = 0;
        for(int j = 0; j <= m; j++){
            if(dp[i][j] == 0) continue;
            int layer = min(m, arr[i] + j);
            dp[i+1][layer] = (dp[i+1][layer] + dp[i][j]) % MOD;
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD;
            if(arr[i] + j + 1 > m){
                total = (total + dp[i][j]) % MOD;
            }
        }
        for(int k = 0; k <= n; k++){
            res[k] = (res[k] + total * comb(n - i - 1, k)) % MOD;
        }
    }

    for(int k = 0; k <= n; k++) cout << res[k] << endl;
}

