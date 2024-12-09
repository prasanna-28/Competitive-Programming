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

void solve() {
    int n, m;
    cin >> n >> m;
    bool seen[n][m];
    vector<vector<int>> grid(n, vector<int>(m));
    for(int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            seen[i][j] = false;
            cin >> grid[i][j];
        }
    }
    i64 res = 0;
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            if(grid[i][j] && !seen[i][j])
            {
                i64 score = 0;
                seen[i][j] = true;
                stack<pair<int, int>> stack;
                stack.push({i, j});
                while(!stack.empty())
                {
                    auto [x, y] = stack.top();
                    stack.pop();
                    score += grid[x][y];
                    if(x > 0 && grid[x-1][y] && !seen[x-1][y])
                    {
                        seen[x-1][y] = true;
                        stack.push({x-1, y});
                    }
                    if(x < n - 1 && grid[x+1][y] && !seen[x+1][y])
                    {
                        seen[x+1][y] = true;
                        stack.push({x+1, y});
                    }
                    if(y > 0 && grid[x][y - 1] && !seen[x][y-1])
                    {
                        seen[x][y-1] = true;
                        stack.push({x, y - 1});
                    }
                    if(y < m - 1 && grid[x][y + 1] && !seen[x][y+1])
                    {
                        seen[x][y+1] = true;
                        stack.push({x, y + 1});
                    }
                }
                res = max(res, score);
            }
        }
    }
    cout << res << nl;
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
