#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int n = s.size();
    vector<int> pairOf;
    vector<vector<int>> posOfPair(676);

    if (n >= 2) {
        pairOf.resize(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            int l = s[i] - 'a';
            int r = s[i + 1] - 'a';
            pairOf[i] = l * 26 + r;
            posOfPair[pairOf[i]].push_back(i);
        }
    }

    int m;
    cin >> m;
    vector<string> out;

    vector<int> visitedTime(n - 1, -1);
    vector<int> usedPairTime(676, -1);
    vector<int> dist(n - 1);
    int BFS_ID = 0;

    while (m--) {
        int f, t;
        cin >> f >> t;
        f--; t--;

        if (f == t) {
            out.push_back("0");
            continue;
        }

        if (n < 2 || f < 0 || t < 0 || f >= n - 1 || t >= n - 1) {
            out.push_back("-1");
            continue;
        }

        BFS_ID++;
        queue<int> q;
        q.push(f);
        visitedTime[f] = BFS_ID;
        dist[f] = 0;
        int answer = -1;

        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            int dcur = dist[cur];

            for (int delta : {-1, 1}) {
                int nxt = cur + delta;
                if (nxt >= 0 && nxt < n - 1 && visitedTime[nxt] != BFS_ID) {
                    visitedTime[nxt] = BFS_ID;
                    dist[nxt] = dcur + 1;
                    if (nxt == t) {
                        answer = dist[nxt];
                        break;
                    }
                    q.push(nxt);
                }
            }
            if (answer != -1) break;

            int p = pairOf[cur];
            if (usedPairTime[p] != BFS_ID) {
                usedPairTime[p] = BFS_ID;
                for (int nxt : posOfPair[p]) {
                    if (visitedTime[nxt] != BFS_ID) {
                        visitedTime[nxt] = BFS_ID;
                        dist[nxt] = dcur + 1;
                        if (nxt == t) {
                            answer = dist[nxt];
                            break;
                        }
                        q.push(nxt);
                    }
                }
                if (answer != -1) break;
            }
        }

        if (answer == -1) {
            answer = (visitedTime[t] == BFS_ID) ? dist[t] : -1;
        }
        out.push_back(to_string(answer));
    }

    for (const string& line : out) {
        cout << line << '\n';
    }
    cout << endl;

    return 0;
}
