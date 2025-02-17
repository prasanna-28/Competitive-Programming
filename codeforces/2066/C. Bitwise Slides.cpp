#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace std;
using namespace __gnu_pbds;

struct custom_hash {
    using ull = unsigned long long;
    static ull splitmix64(ull x) {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }
    size_t operator()(unsigned long long x) const {
        static const ull FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

const long long MOD = 1000000007;

void solveTest(){
    int n;
    cin >> n;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    gp_hash_table<long long, long long, custom_hash> dp;
    long long neutral = 1;
    for (int i = 0; i < n; i++){
        long long a = arr[i];
        gp_hash_table<long long, long long, custom_hash> new_dp;
        long long newNeutral = 0;
        for(auto &p : dp){
            long long key = p.first, ways = p.second;
            if(key == a){
                new_dp[a] = (new_dp[a] + (2 * ways) % MOD) % MOD;
                newNeutral = (newNeutral + ways) % MOD;
            } else {
                long long nk = key ^ a;
                new_dp[nk] = (new_dp[nk] + ways) % MOD;
            }
        }
        new_dp[a] = (new_dp[a] + (3 * neutral) % MOD) % MOD;
        dp = move(new_dp);
        neutral = newNeutral;
    }
    long long ans = neutral;
    for(auto &p : dp)
        ans = (ans + p.second) % MOD;
    cout << ans % MOD << "\n";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--){
        solveTest();
    }
    cout << endl;
    return 0;
}


