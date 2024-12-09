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


#include <iostream>
#include <vector>
#include <algorithm>

const int MAX_N = 1e7 + 1;

std::vector<int> sieve_and_grundy(int n) {
    std::vector<bool> is_prime(n + 1, true);
    std::vector<int> smallest_prime_factor(n + 1);
    std::vector<int> grundy(n + 1, 0);

    is_prime[0] = is_prime[1] = false;
    grundy[1] = 1;
    int primes = 0;

    for (int i = 0; i <= n; ++i) {
        smallest_prime_factor[i] = i;
    }

    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            primes++;
            grundy[i] = (i != 2) ? primes : 0;
            for (int j = i * i; j <= n; j += i) {
                if (is_prime[j]) {
                    is_prime[j] = false;
                    smallest_prime_factor[j] = i;
                }
            }
        } else {
            grundy[i] = grundy[smallest_prime_factor[i]];
        }
    }

    return grundy;
}

std::vector<int> grundy = sieve_and_grundy(MAX_N);

void solve() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int xor_sum = 0;
    for (int num : a) {
        xor_sum ^= grundy[num];
    }

    if (xor_sum == 0) {
        std::cout << "Bob" << std::endl;
    } else {
        std::cout << "Alice" << std::endl;
    }
}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc;
    if(MT) cin >> tc;
    else tc = 1;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
    cout << endl;
}
