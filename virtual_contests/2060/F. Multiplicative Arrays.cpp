#include <bits/stdc++.h>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    cin >> N >> Q;

    vector<int> a(N+1);
    for(int i = 1; i <= N; i++){
        cin >> a[i];
    }

    vector< set<int> > positions(N+1);

    for(int i = 1; i <= N; i++){
        positions[a[i]].insert(i);
    }

    while(Q--) {
        int t;
        cin >> t;
        if(t == 1) {
            int x, y;
            cin >> x >> y;
            int oldVal = a[x];
            if(oldVal != y) {
                positions[oldVal].erase(x);
                positions[y].insert(x);
                a[x] = y;
            }
        }
        else {
            int l, r;
            cin >> l >> r;

            int left = 1, right = N;
            int answer = 1;

            while(left <= right) {
                int mid = (left + right) / 2;

                auto it = positions[mid].lower_bound(l);

                bool isMissing = false;
                if(it == positions[mid].end() || *it > r) {
                    isMissing = true;
                }

                if(isMissing) {
                    answer = mid;

                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            cout << answer << endl;
        }
    }

    return 0;
}

