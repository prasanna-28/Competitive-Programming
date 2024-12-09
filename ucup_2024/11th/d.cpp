#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MOD = 998244353;

ll power_pow(ll a, ll b) {
    ll res = 1;
    a %= MOD;
    while(b > 0){
        if(b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>=1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, M, Q;
    cin >> N >> M >> Q;
    vector<int> A(N);
    for(auto &x:A) cin>>x;
    int total = 1<<M;
    vector<int> dp_prev(total, 0);
    dp_prev[0] = 1;
    vector<int> C(N);
    for(int i=0;i<N;i++) C[i] = (A[i]==0)?0 : ((1<<A[i]) -1);
    for(int i=0;i<N;i++){
        vector<int> dp_curr(total, 0);
        int Ci = C[i];
        for(int S=0; S < total; S++){
            if(dp_prev[S]==0) continue;
            for(int x=0; x<M; x++){
                int S_new = S ^ (1<<x);
                if( (S_new & (~Ci)) ==0 ){
                    dp_curr[S_new] = (dp_curr[S_new] + dp_prev[S])%MOD;
                }
            }
        }
        dp_prev = move(dp_curr);
    }
    ll initial_ans = 0;
    for(auto x: dp_prev) initial_ans = (initial_ans + x)%MOD;
    while(Q--){
        int xi, yi;
        cin >> xi >> yi;
        A[xi-1] = yi;
        for(int i=0;i<N;i++) C[i] = (A[i]==0)?0 : ((1<<A[i]) -1);
        vector<int> dp_prev_new(total, 0);
        dp_prev_new[0] = 1;
        for(int i=0;i<N;i++){
            vector<int> dp_curr(total, 0);
            int Ci_new = C[i];
            for(int S=0; S < total; S++){
                if(dp_prev_new[S]==0) continue;
                for(int x=0; x<M; x++){
                    int S_new = S ^ (1<<x);
                    if( (S_new & (~Ci_new)) ==0 ){
                        dp_curr[S_new] = (dp_curr[S_new] + dp_prev_new[S])%MOD;
                    }
                }
            }
            dp_prev_new = move(dp_curr);
        }
        ll ans =0;
        for(auto x: dp_prev_new) ans = (ans + x)%MOD;
        cout << ans << endl;
    }
}

