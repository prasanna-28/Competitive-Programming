#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<pair<ll, ll>> cities(n);
        for (auto& [a, b] : cities) cin >> a >> b;
        sort(cities.begin(), cities.end(), [](const pair<ll, ll>& x, const pair<ll, ll>& y) {
            return (x.first - x.second) > (y.first - y.second);
        });
        vector<ll> sum_a(n + 1), sum_b(n + 1);
        for (int i = 0; i < n; ++i) {
            sum_a[i + 1] = sum_a[i] + cities[i].first;
            sum_b[i + 1] = sum_b[i] + cities[i].second;
        }
        vector<ll> ans;
        for (int k = 2; k <= n; ++k) {
            ll current = 0;
            ll max_a = 0, max_b = 0;
            for (int i = 0; i < k; ++i) {
                max_a = max(max_a, cities[i].first);
                max_b = max(max_b, cities[i].second);
            }
            current = (sum_a[k] + sum_b[k]) - max_a - max_b;
            ans.push_back(current);
        }
        for (ll x : ans) cout << x << ' ';
        cout << endl;
    }
    return 0;
}
