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

#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 20;
static const int MAXQ = 200000;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;


    static int E[MAXN+1][MAXQ+1];
    static int S[MAXN+1][MAXQ+1];
    for(int i=1; i<=n; i++){
        for(int t=0; t<=q; t++){
            E[i][t] = 0;
            S[i][t] = 0;
        }
    }

    vector<int> who(q+1);
    vector<bool> isPlus(q+1);

    for(int t=1; t<=q; t++){
        int si; char c;
        cin >> si >> c;
        who[t] = si;
        isPlus[t] = (c == '+');
    }

    for(int t=1; t<=q; t++){
        for(int i=1; i<=n; i++){
            E[i][t] = E[i][t-1];
            S[i][t] = S[i][t-1];
        }
        int snakeId = who[t];
        if(isPlus[t]) {
            E[snakeId][t] = E[snakeId][t-1] + 1;
            S[snakeId][t] = S[snakeId][t-1];
        } else {
            S[snakeId][t] = S[snakeId][t-1] + 1;
            E[snakeId][t] = E[snakeId][t-1];
        }
    }

    vector<int> MxE(n+1, 0);
    for(int i=1; i<=n; i++){
        int mx = 0;
        for(int t=0; t<=q; t++){
            mx = max(mx, E[i][t]);
        }
        MxE[i] = mx;
    }

    static int D[MAXN+1][MAXN+1];
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i == j){
                D[i][j] = 1 + 0;
            } else {
                int val = INT_MIN;
                for(int t=0; t<=q; t++){
                    val = max(val, E[i][t] - S[j][t]);
                }
                D[i][j] = val + 1;
            }
        }
    }

    vector<vector<long long>> dp_maxC(1<<n, vector<long long>(n, LLONG_MAX));
    vector<vector<int>> dp_offset(1<<n, vector<int>(n, INT_MAX));

    for(int i=0; i<n; i++){
        int mask = (1 << i);
        dp_offset[mask][i] = 0;
        dp_maxC[mask][i] = 1LL + (long long)(MxE[i+1]);
    }

    for(int mask=0; mask < (1<<n); mask++){
        for(int prev=0; prev<n; prev++){
            if(!(mask & (1<<prev))) continue;
            long long currMaxC = dp_maxC[mask][prev];
            int currOffset = dp_offset[mask][prev];
            if(currMaxC == LLONG_MAX) continue;

            int others = ((1<<n) -1) ^ mask;
            while(others){
                int j = __builtin_ctz(others);
                others ^= (1<<j);

                int dist = D[prev+1][j+1];
                long long newOffset = (long long)currOffset + dist;
                long long newMaxC = max(currMaxC, 1 + newOffset + (long long)MxE[j+1]);

                int newMask = mask | (1<<j);
                if(newMaxC < dp_maxC[newMask][j]){
                    dp_maxC[newMask][j] = newMaxC;
                    dp_offset[newMask][j] = (int)newOffset;
                }
                else if(newMaxC == dp_maxC[newMask][j]){
                    dp_offset[newMask][j] = min(dp_offset[newMask][j], (int)newOffset);
                }
            }
        }
    }

    long long ans = LLONG_MAX;
    int fullMask = (1<<n) - 1;
    for(int last=0; last<n; last++){
        ans = min(ans, dp_maxC[fullMask][last]);
    }

    cout << ans << endl;
    return 0;
}
