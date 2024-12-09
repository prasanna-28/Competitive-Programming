#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

const ll INF = 1e18;
const ll NINF = -1e18;

struct SegmentTree {
    typedef ll T;
    ll size;
    T default_value;
    T (*func)(T, T);
    vector<T> data;

    SegmentTree() {}

    SegmentTree(ll n, T default_value, T (*func)(T, T)) {
        this->default_value = default_value;
        this->func = func;
        size = 1;
        while (size < n) size <<= 1;
        data.assign(2 * size, default_value);
    }

    void build(vector<T>& v) {
        for (size_t i = 0; i < v.size(); ++i)
            data[i + size] = v[i];
        for (ll i = size - 1; i > 0; --i)
            data[i] = func(data[2 * i], data[2 * i + 1]);
    }

    void update(ll idx, T value) {
        idx += size;
        data[idx] = value;
        while (idx > 1) {
            idx >>= 1;
            data[idx] = func(data[2 * idx], data[2 * idx + 1]);
        }
    }

    T query(ll l, ll r) { // [l, r)
        l += size;
        r += size;
        T res_left = default_value;
        T res_right = default_value;
        while (l < r) {
            if (l & 1) res_left = func(res_left, data[l++]);
            if (r & 1) res_right = func(data[--r], res_right);
            l >>= 1;
            r >>= 1;
        }
        return func(res_left, res_right);
    }
};

ll max_func(ll a, ll b) {
    return max(a, b);
}

ll min_func(ll a, ll b) {
    return min(a, b);
}

void solve() {
    ll n;
    cin >> n;
    vector<pll> lrs(n);
    vector<pll> idxes(n);
    for (ll i = 0; i < n; ++i) {
        ll l, r;
        cin >> l >> r;
        lrs[i] = {l, r};
        idxes[i] = {l, r};
    }

    // First sorting
    sort(lrs.begin(), lrs.end(), [](const pll& a, const pll& b) {
        if (a.first == b.first)
            return a.second > b.second;
        return a.first < b.first;
    });

    vector<ll> r_values;
    for (auto& p : lrs) {
        r_values.push_back(p.first);
        r_values.push_back(p.second);
    }
    sort(r_values.begin(), r_values.end());
    r_values.erase(unique(r_values.begin(), r_values.end()), r_values.end());

    unordered_map<ll, ll> normalize;
    for (size_t i = 0; i < r_values.size(); ++i) {
        normalize[r_values[i]] = i;
    }

    ll size = r_values.size() + 5;
    SegmentTree segtreel(size, NINF, max_func);
    SegmentTree segtreer(size, INF, min_func);
    vector<ll> empty_l(size, NINF);
    vector<ll> empty_r(size, INF);
    segtreel.build(empty_l);
    segtreer.build(empty_r);

    map<pll, ll> res;
    map<pll, ll> res2;

    for (auto& p : lrs) {
        ll l = p.first;
        ll r = p.second;
        ll k = normalize[r];
        ll left = segtreel.query(k, size);
        res[{l, r}] = left;
        segtreel.update(k, l);
    }

    // Second sorting
    sort(lrs.begin(), lrs.end(), [](const pll& a, const pll& b) {
        if (a.second == b.second)
            return a.first < b.first;
        return a.second > b.second;
    });

    for (auto& p : lrs) {
        ll l = p.first;
        ll r = p.second;
        ll k = normalize[l];
        ll right = segtreer.query(0, k + 1);
        res2[{l, r}] = right;
        segtreer.update(k, r);
    }

    map<pll, ll> idx_map;
    for (ll i = 0; i < n; ++i) {
        idx_map[idxes[i]] = i;
    }

    vector<ll> output(n);
    for (auto& k : idxes) {
        ll l = k.first;
        ll r = k.second;
        if (res[k] == NINF || res2[k] == INF) {
            output[idx_map[k]] = 0;
            continue;
        }
        ll value = res2[k] - res[k] + 1 - (r - l + 1);
        output[idx_map[k]] = max(0LL, value);
    }
    for (ll i = 0; i < n; ++i) {
        cout << output[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;
    while (t--) {
        solve();
    }
    cout << endl;
    return 0;
}

