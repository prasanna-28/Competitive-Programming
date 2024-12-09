#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    while (q--) {
        int i, x;
        cin >> i >> x;
        i--;

        int level = 1;
        int fights = 0;

        for (int j = 0; j <= i; j++) {
            if (level <= a[j]) {
                fights++;
                if (fights % x == 0) {
                    level++;
                }
            }
        }

        cout << (level < a[i] ? "YES" : "NO") << "\n";
    }
    cout << endl;

    return 0;
}
