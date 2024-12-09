#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAX_M = 5005;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m_input;
    cin >> n >> m_input;
    vector<int> r(n);
    for (int i = 0; i < n; ++i) cin >> r[i];

    vector<int> zeros_positions;
    for (int i = 0; i < n; ++i)
        if (r[i] == 0) zeros_positions.push_back(i);
    int m = zeros_positions.size();

    vector<int> seg_start(m + 2);
    seg_start[0] = -1;
    for (int i = 0; i < m; ++i) seg_start[i + 1] = zeros_positions[i];
    seg_start[m + 1] = n;

    vector<vector<int>> counts_int(m + 1, vector<int>(MAX_M, 0));
    vector<vector<int>> counts_str(m + 1, vector<int>(MAX_M, 0));
    vector<vector<int>> prefix_int(m + 1, vector<int>(MAX_M, 0));
    vector<vector<int>> prefix_str(m + 1, vector<int>(MAX_M, 0));

    for (int k = 0; k <= m; ++k) {
        int start = seg_start[k] + 1;
        int end = seg_start[k + 1];
        vector<int> int_checks, str_checks;
        for (int i = start; i < end; ++i) {
            int ri = r[i];
            if (ri > 0) {
                if (ri < MAX_M) counts_int[k][ri]++;
            } else if (ri < 0) {
                int level = -ri;
                if (level < MAX_M) counts_str[k][level]++;
            }
        }
        prefix_int[k][0] = counts_int[k][0];
        prefix_str[k][0] = counts_str[k][0];
        for (int i = 1; i < MAX_M; ++i) {
            prefix_int[k][i] = prefix_int[k][i - 1] + counts_int[k][i];
            prefix_str[k][i] = prefix_str[k][i - 1] + counts_str[k][i];
        }
    }


    vector<vector<int>> dp(m + 1, vector<int>(m + 1, -1));
    dp[0][0] = 0;

    for (int k = 0; k < m; ++k) {
        for (int s = 0; s <= k; ++s) {
            if (dp[k][s] == -1) continue;
            int current_passed = dp[k][s];
            int s_new = s + 1;
            if (s_new <= k + 1) {
                int int_level = (k + 1) - s_new;
                int passed_checks = 0;
                if (int_level >= MAX_M) {
                    passed_checks += prefix_int[k + 1][MAX_M - 1];
                } else {
                    passed_checks += prefix_int[k + 1][int_level];
                }
                if (s_new >= MAX_M) {
                    passed_checks += prefix_str[k + 1][MAX_M - 1];
                } else {
                    passed_checks += prefix_str[k + 1][s_new];
                }
                int total_passed = current_passed + passed_checks;
                dp[k + 1][s_new] = max(dp[k + 1][s_new], total_passed);
            }
            s_new = s;
            int int_level = (k + 1) - s_new;
            int passed_checks = 0;
            if (int_level >= MAX_M) {
                passed_checks += prefix_int[k + 1][MAX_M - 1];
            } else {
                passed_checks += prefix_int[k + 1][int_level];
            }
            if (s_new >= MAX_M) {
                passed_checks += prefix_str[k + 1][MAX_M - 1];
            } else {
                passed_checks += prefix_str[k + 1][s_new];
            }
            int total_passed = current_passed + passed_checks;
            dp[k + 1][s_new] = max(dp[k + 1][s_new], total_passed);
        }
    }

    int max_passed = 0;
    for (int s = 0; s <= m; ++s)
        if (dp[m][s] > max_passed)
            max_passed = dp[m][s];

    cout << max_passed << endl;
    return 0;
}

