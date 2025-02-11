#include <bits/stdc++.h>
using namespace std;

static const int MAXM = 10;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, m, k;
        cin >> n >> m >> k;

        vector<uint32_t> a(n);
        for(int i=0; i<n; i++){
            cin >> a[i];
        }

        vector<uint32_t> b(m);
        for(int j=0; j<m; j++){
            cin >> b[j];
        }

        int numSub = (1 << m);
        vector<uint32_t> subsetAnd(numSub, 0);
        vector<int> subsetSize(numSub, 0);

        subsetAnd[0] = ~0u;
        subsetSize[0] = 0;
        for(int s=1; s<numSub; s++){
            int lb = __builtin_ctz(s);
            int sWithoutLb = s ^ (1 << lb);
            subsetAnd[s] = subsetAnd[sWithoutLb] & b[lb];
            subsetSize[s] = subsetSize[sWithoutLb] + 1;
        }

        vector<long long> improvements;
        improvements.reserve(n * m);

        long long sumA = 0;
        for(int i=0; i<n; i++){
            sumA += a[i];

            static uint32_t cost[ MAXM + 1 ];
            for(int r=1; r<=m; r++){
                cost[r] = UINT32_MAX;
            }
            cost[0] = a[i];

            for(int s=1; s<numSub; s++){
                int ssz = subsetSize[s];
                if(ssz <= m){
                    uint32_t candidate = a[i] & subsetAnd[s];
                    if(candidate < cost[ssz]){
                        cost[ssz] = candidate;
                    }
                }
            }
            for(int r=1; r<=m; r++){
                if(cost[r-1] < cost[r]){
                    cost[r] = cost[r-1];
                }
            }

            for(int r=1; r<=m; r++){
                long long diff = (long long)cost[r-1] - (long long)cost[r];
                if(diff > 0){
                    improvements.push_back(diff);
                }
            }
        }

        sort(improvements.begin(), improvements.end(), greater<long long>());

        long long answer = sumA;
        for(int i=0; i < (int)improvements.size() && i<k; i++){
            long long gain = improvements[i];
            if(gain <= 0) break;
            answer -= gain;
        }

        cout << answer << endl;

        improvements.clear();
    }

    return 0;
}

