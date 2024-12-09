#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int p, x;
vector<int> fact, invfact;

int pow_mod(int base, int exp, int mod) {
    int result = 1;
    while (exp > 0) {
        if (exp & 1) result = (1LL * result * base) % mod;
        base = (1LL * base * base) % mod;
        exp >>= 1;
    }
    return result;
}

void precompute() {
    fact.resize(p);
    invfact.resize(p);
    fact[0] = 1;
    for (int i = 1; i < p; i++) {
        fact[i] = (1LL * fact[i-1] * i) % p;
    }
    invfact[p-1] = pow_mod(fact[p-1], p-2, p);
    for (int i = p-2; i >= 0; i--) {
        invfact[i] = (1LL * invfact[i+1] * (i+1)) % p;
    }
}

int nCr(int n, int r) {
    if (r > n) return 0;
    return (1LL * fact[n] * invfact[r] % p) * invfact[n-r] % p;
}

vector<int> convolve(const vector<int>& a, const vector<int>& b) {
    vector<int> result(p);
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < p; j++) {
            result[(i + j) % p] = (result[(i + j) % p] + 1LL * a[i] * b[j]) % MOD;
        }
    }
    return result;
}

vector<int> calc_digit_state() {
    vector<int> state(p);
    for (int i = 0; i < p; i++) {
        for (int j = 0; j <= i; j++) {
            state[nCr(i, j)]++;
        }
    }
    return state;
}

int solve(const string& k) {
    vector<int> state(p);
    state[1] = 1;  // Initial state
    vector<int> digit_state = calc_digit_state();

    vector<int> power_states(k.length() + 1, vector<int>(p));
    power_states[0] = state;

    for (int i = 1; i <= k.length(); i++) {
        power_states[i] = convolve(power_states[i-1], digit_state);
    }

    vector<int> result(p);
    for (int i = 0; i < k.length(); i++) {
        if (k[i] == '1') {
            result = convolve(result, power_states[k.length() - 1 - i]);
        }
    }

    return result[x];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string k;
    cin >> k >> p >> x;

    precompute();
    cout << solve(k) << "\n";

    return 0;
}
