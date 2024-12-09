#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MOD = 998244353;

vector<vector<ll>> multiply(const vector<vector<ll>> &a, const vector<vector<ll>> &b) {
    int n = a.size();
    int m = a[0].size();
    int p = b[0].size();
    vector<vector<ll>> res(n, vector<ll>(p, 0));
    for(int i=0;i<n;i++) {
        for(int k=0;k<m;k++) {
            if(a[i][k] == 0) continue;
            for(int j=0;j<p;j++) {
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD;
            }
        }
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    vector<ll> queries(T);
    for(auto &x: queries) cin >> x;

    string tgtA = "NPCAPC";
    string tgtB = "npcapc";
    int lenA = tgtA.size(); // 6
    int lenB = tgtB.size(); // 6

    auto getIndex = [&](int i, int j) -> int {
        return i * (lenB +1) + j;
    };

    int tsts = (lenA +1) * (lenB +1); // 49

    vector<vector<ll>> trans(tsts, vector<ll>(tsts, 0));

    for(int i=0;i<=lenA;i++) {
        for(int j=0;j<=lenB;j++) {
            int current = getIndex(i, j);

            if(i < lenA){
                int ni = i +1;
                int nj = j;
                int next_idx = getIndex(ni, nj);
                trans[next_idx][current] = (trans[next_idx][current] + 1) % MOD;
            }

            if(j < lenB){
                int ni = i;
                int nj = j +1;
                int next_idx = getIndex(ni, nj);
                trans[next_idx][current] = (trans[next_idx][current] + 1) % MOD;
            }

            int nmtch = 52;
            if(i < lenA) nmtch -=1;
            if(j < lenB) nmtch -=1;
            trans[current][current] = (trans[current][current] + (ll)(nmtch % MOD)) % MOD;
        }
    }

    vector<vector<vector<ll>>> precp;
    precp.push_back(trans);
    for(int p=1; p < 32; p++){
        precp.push_back(multiply(precp[p-1], precp[p-1]));
    }

    for(auto N: queries){
        vector<ll> dp(tsts, 0);
        dp[getIndex(0,0)] = 1;

        int power =0;
        ll current_N = N;
        while(current_N >0){
            if(current_N &1){
                vector<ll> ndp(tsts, 0);
                const vector<vector<ll>> &mat = precp[power];
                for(int y=0;y<tsts;y++){
                    for(int x=0;x<tsts;x++){
                        if(mat[y][x] ==0 || dp[x]==0) continue;
                        ndp[y] = (ndp[y] + mat[y][x] * dp[x]) % MOD;
                    }
                }
                dp = move(ndp);
            }
            current_N >>=1;
            power++;
        }

        ll ans = dp[getIndex(lenA, lenB)];
        cout << ans << endl;
    }
}

