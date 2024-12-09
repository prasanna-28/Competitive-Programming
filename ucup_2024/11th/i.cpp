#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MOD = 998244353;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    vector<int> A(N);
    for(auto &x: A) cin >> x;

    ll S = 0;
    for(auto x : A) S += x;

    if(S % 2 != 0){
        cout << "0\n";
        return 0;
    }

    ll target = S / 2;

    vector<vector<long long>> dp(N+1, vector<long long>(target+1, 0));
    dp[0][0] = 1;

    for(auto a : A){
        for(int i = N; i >=1; --i){
            for(ll s = target; s >= a; --s){
                dp[i][s] = (dp[i][s] + dp[i-1][s - a]) % MOD;
            }
        }
    }

    vector<long long> fact(N+1, 1);
    for(int i = 1; i <= N; i++) {
        fact[i] = (fact[i-1] * i) % MOD;
    }

    ll ans = 0;
    for(int i = 1; i < N; i++){
        if(dp[i][target] > 0){
            ll term = (dp[i][target] * fact[i]) % MOD;
            term = (term * fact[N-i]) % MOD;
            ans = (ans + term) % MOD;
        }
    }

    cout << ans<<endl;
}

