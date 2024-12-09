#include <bits/stdc++.h>
using namespace std;

#define i64 long long
#define i32 int
#define u32 unsigned int
#define u64 unsigned long long
#define len(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const i64 MOD = 1e9 + 7;
const i64 INF = 1e9;
const i64 NINF = -(1e9);
const i32 MT = 1;
const char nl = '\n';

namespace std {
    template <typename T>
    struct MultiDimVector : public vector<T> {
        MultiDimVector(int n = 0, T val = T()) : vector<T>(n, val) {}
    };

    template <int D, typename T>
    struct MultiDimVector<D, T> : public vector<MultiDimVector<D - 1, T>> {
        template <typename... Args>
        MultiDimVector(int n = 0, Args... args) : vector<MultiDimVector<D - 1, T>>(n, MultiDimVector<D - 1, T>(args...)) {}
    };

    template <class Function>
    class recursive_lambda {
        Function func_;
    public:
        template <class T>
        explicit recursive_lambda(T &&func) : func_(forward<T>(func)) {}

        template <class... Args>
        decltype(auto) operator()(Args &&...args) {
            return func_(ref(*this), forward<Args>(args)...);
        }
    };

    template <class Function>
    decltype(auto) make_recursive_lambda(Function &&func) {
        return recursive_lambda<decay_t<Function>>(forward<Function>(func));
    }
}

void solve() {
    i32 n, q;
    cin >> n >> q;
    vector<i32> a(n, -1), p(n), ps(n);
    for (i32 i = 1; i < n; i++) cin >> a[i], a[i]--;
    for (i32 i = 0; i < n; i++) cin >> p[i], p[i]--, ps[p[i]] = i;

    i32 bd = 0;
    vector<set<i32>> s(n);
    vector<i32> f(n);
    vector<vector<i32>> adj(n);

    auto dfs = make_recursive_lambda([&](auto& self, i32 v) -> void {
        f[v] = 1;
        for (i32 u : adj[v]) {
            self(self, u);
            f[v] += f[u];
        }
    });

    for (i32 i = 1; i < n; i++) adj[a[i]].push_back(i);
    dfs(dfs, 0);

    auto chk = [&](i32 i) {
        return !s[i].empty() && *s[i].begin() < ps[i];
    };

    auto rm = [&](i32 i, i32 x) {
        auto it = s[i].find(x);
        i32 l = it != s[i].begin() ? *prev(it) : -1;
        i32 r = next(it) != s[i].end() ? *next(it) : -1;
        if (l != -1 && l + f[p[l]] != x) bd--;
        if (r != -1 && x + f[p[x]] != r) bd--;
        if (l != -1 && r != -1 && l + f[p[l]] != r) bd++;
        s[i].erase(it);
    };

    auto add = [&](i32 i, i32 x) {
        s[i].insert(x);
        auto it = s[i].find(x);
        i32 l = it != s[i].begin() ? *prev(it) : -1;
        i32 r = next(it) != s[i].end() ? *next(it) : -1;
        if (l != -1 && l + f[p[l]] != x) bd++;
        if (r != -1 && x + f[p[x]] != r) bd++;
        if (l != -1 && r != -1 && l + f[p[l]] != r) bd--;
    };

    for (i32 i = 0; i < n; i++)
        if (a[p[i]] != -1) add(a[p[i]], i);
    for (i32 i = 0; i < n; i++)
        bd += chk(i);

    while (q--) {
        i32 x, y;
        cin >> x >> y;
        x--, y--;
        set<i32> ch = {p[x], p[y], a[p[x]], a[p[y]]};
        for (i32 z : ch)
            if (z != -1) bd -= chk(z);
        if (a[p[x]] != -1) rm(a[p[x]], x);
        if (a[p[y]] != -1) rm(a[p[y]], y);
        swap(p[x], p[y]);
        swap(ps[p[x]], ps[p[y]]);
        if (a[p[x]] != -1) add(a[p[x]], x);
        if (a[p[y]] != -1) add(a[p[y]], y);
        for (i32 z : ch)
            if (z != -1) bd += chk(z);
        cout << (bd ? "NO" : "YES") << nl;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    i32 tc = 1;
    if(MT) cin >> tc;
    while (tc--) solve();
    cout << endl;
}
