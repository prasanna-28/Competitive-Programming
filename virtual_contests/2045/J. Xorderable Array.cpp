#include <bits/stdc++.h>
using namespace std;
const int B_MAX = 30;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<string> a(n), b(m);
    for (int i = 0; i < n; i++){
        long long x;
        cin >> x;
        a[i] = bitset<B_MAX>(x).to_string();
    }
    for (int i = 0; i < m; i++){
        long long x;
        cin >> x;
        b[i] = bitset<B_MAX>(x).to_string();
    }
    long long res = 0;
    vector<int> trie_A, trie_X;
    trie_A.resize(3); trie_A[0] = trie_A[1] = -1; trie_A[2] = 0;
    trie_X.resize(3); trie_X[0] = trie_X[1] = -1; trie_X[2] = 0;
    int depth = -1;
    for (auto &s : a) {
        int node = 0;
        trie_A[node + 2]++;
        for (int idx = 0; idx < B_MAX; idx++){
            int bit = s[idx] - '0';
            if (trie_A[node + bit] != -1) {
                node = 3 * trie_A[node + bit];
                trie_A[node + 2]++;
                if (trie_A[node + (bit ^ 1)] != -1)
                    depth = max(depth, idx);
            } else {
                if (trie_A[node + (bit ^ 1)] != -1)
                    depth = max(depth, idx);
                int new_node_index = trie_A.size() / 3;
                trie_A[node + bit] = new_node_index;
                trie_A.push_back(-1);
                trie_A.push_back(-1);
                trie_A.push_back(1);
                node = 3 * new_node_index;
            }
        }
    }
    vector<int> diffs;
    diffs.push_back(depth);
    unordered_map<string, vector<string>> pairs;
    for (auto &s : a){
        string prefix = (depth <= 0 ? "" : s.substr(0, depth));
        pairs[prefix].push_back(s);
    }
    unordered_map<int, vector<int>> lmap;
    for (auto &p : pairs) {
        if (p.second.size() != 2) continue;
        string p1 = p.second[0], p2 = p.second[1];
        int d = 0;
        for (int i = depth + 1; i < B_MAX; i++){
            if (p1[i] != p2[i]){
                lmap[d].push_back(i);
                d++;
            }
        }
    }
    int prev_val = depth;
    vector<int> keys;
    for (auto &kv : lmap)
        keys.push_back(kv.first);
    sort(keys.begin(), keys.end());
    for (auto d : keys) {
        int curr = prev_val;
        for (auto i : lmap[d])
            curr = max(curr, i);
        if (curr == prev_val)
            break;
        prev_val = curr;
        diffs.push_back(curr);
    }
    sort(diffs.begin(), diffs.end());
    diffs.erase(unique(diffs.begin(), diffs.end()), diffs.end());
    vector<bool> diffMark(B_MAX, false);
    for (auto d : diffs)
        if (d >= 0 && d < B_MAX)
            diffMark[d] = true;
    for (auto &s : b) {
        int node = 0;
        for (int idx = 0; idx < B_MAX; idx++){
            int bit = s[idx] - '0';
            if (diffMark[idx]) {
                if (trie_X[node + bit] != -1) {
                    int child_index = trie_X[node + bit];
                    res += trie_X[child_index * 3 + 2];
                }
                if (trie_X[node + (bit ^ 1)] != -1) {
                    node = trie_X[node + (bit ^ 1)] * 3;
                } else {
                    break;
                }
            } else {
                if (trie_X[node + bit] != -1)
                    node = trie_X[node + bit] * 3;
                else
                    break;
            }
        }
        node = 0;
        trie_X[node + 2]++;
        for (int i = 0; i < B_MAX; i++){
            int bit = s[i] - '0';
            if (trie_X[node + bit] != -1) {
                node = trie_X[node + bit] * 3;
                trie_X[node + 2]++;
            } else {
                int new_node_index = trie_X.size() / 3;
                trie_X[node + bit] = new_node_index;
                trie_X.push_back(-1);
                trie_X.push_back(-1);
                trie_X.push_back(1);
                node = new_node_index * 3;
            }
        }
    }
    cout << res << "\n";
    return 0;
}

