#include <bits/stdc++.h>
using namespace std;

// Type definitions for convenience
#define i64 long long
#define i32 int
#define u32 unsigned int
#define u64 unsigned long long

// Utility macros
#define len(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

// Constants
const i64 MOD  = 1e9 + 7;
const i64 INF  = 1e9;
const i64 NINF = -(1e9);
const i32 MT   = 1; // Set to 1 if multiple test cases are expected

const char nl  = '\n';

// Structure to represent an interval
struct Interval {
    int start, end;
    bool is_valid;

    // Comparator for ordering intervals in the set
    bool operator<(const Interval& other) const {
        if (start != other.start)
            return start < other.start;
        return end < other.end;
    }
};

int solve(){
    int n, q;
    cin >> n >> q; // Read number of elements and queries

    vector<int> p(n);
    for(auto &x: p) cin >> x; // Read permutation array

    string s;
    cin >> s; // Read the connection string

    // Ensure the connection string has exactly n-1 characters
    if(len(s) != n-1){
        // Handle unexpected string lengths if necessary
        // For this correction, we assume the input is correct
    }

    // Position array to store the index of each element in the permutation
    vector<int> pos(n+1);
    for(int i=0; i<n; ++i){
        pos[p[i]] = i+1;
    }

    // Set to store connected intervals
    set<Interval> connected;
    int start = 1;

    // Initial construction of connected intervals based on the connection string
    for(int i=1; i<n; ++i){
        // Avoid out-of-bounds by ensuring 'i < n-1' before accessing s[i]
        if(i < n-1 && (s[i-1] == 'R' || s[i] == 'L')){
            continue; // Continue the current interval
        }
        else{
            // Determine the current interval [start, i]
            int min_p = *min_element(p.begin()+start-1, p.begin()+i);
            int max_p = *max_element(p.begin()+start-1, p.begin()+i);
            bool is_valid = (min_p >= start && max_p <= i);
            connected.insert(Interval{start, i, is_valid});
            start = i+1; // Start a new interval
        }
    }

    // Handle the last interval if any
    if(start <= n){
        int min_p = *min_element(p.begin()+start-1, p.begin()+n);
        int max_p = *max_element(p.begin()+start-1, p.begin()+n);
        bool is_valid = (min_p >= start && max_p <= n);
        connected.insert(Interval{start, n, is_valid});
    }

    // Count the number of invalid intervals initially
    int invalid_count = 0;
    for(auto &interval: connected){
        if(!interval.is_valid) invalid_count++;
    }

    // Process each query
    while(q--){
        int i;
        cin >> i; // Read the position to toggle

        // Toggle the character at position i-1
        s[i-1] = (s[i-1] == 'L') ? 'R' : 'L';

        // The connections affected by this toggle are (i-1, i) and (i, i+1)
        vector<pair<int, int>> connections = { {i-1, i}, {i, i+1} };

        for(auto &[a, b]: connections){
            // Skip invalid connections
            if(a < 1 || b > n){
                continue;
            }

            // Determine the new connection status after toggle
            bool connected_now = (s[a-1] == 'R' || s[b-1] == 'L');
            // Determine the previous connection status
            bool was_connected = !connected_now;

            if(!was_connected && connected_now){
                // **Connection Added**: Merge intervals containing 'a' and 'b'

                // Find the interval containing 'a'
                auto it_a = connected.lower_bound(Interval{a, 0, false});
                if(it_a == connected.end() || it_a->start > a){
                    if(it_a == connected.begin()) {
                        // No interval contains 'a'
                        continue;
                    }
                    --it_a;
                }
                if(!(it_a->start <= a && it_a->end >= a)){
                    // No interval contains 'a'
                    continue;
                }

                // Find the interval containing 'b'
                auto it_b = connected.lower_bound(Interval{b, 0, false});
                if(it_b == connected.end() || it_b->start > b){
                    if(it_b == connected.begin()) {
                        // No interval contains 'b'
                        continue;
                    }
                    --it_b;
                }
                if(!(it_b->start <= b && it_b->end >= b)){
                    // No interval contains 'b'
                    continue;
                }

                if(it_a == it_b){
                    // 'a' and 'b' are already in the same interval
                    continue;
                }

                // Merge the two intervals
                // Decrement invalid_count if any of the merged intervals were invalid
                if(!it_a->is_valid) invalid_count--;
                if(!it_b->is_valid) invalid_count--;

                int new_start = it_a->start;
                int new_end = it_b->end;

                // Calculate the new validity of the merged interval
                int min_p = *min_element(p.begin()+new_start-1, p.begin()+new_end);
                int max_p = *max_element(p.begin()+new_start-1, p.begin()+new_end);
                bool is_valid = (min_p >= new_start && max_p <= new_end);

                // Erase the old intervals
                connected.erase(it_a);
                connected.erase(it_b);

                // Insert the merged interval
                connected.insert(Interval{new_start, new_end, is_valid});
                if(!is_valid){
                    invalid_count++;
                }
            }
            else if(was_connected && !connected_now){
                // **Connection Removed**: Split the interval containing [a, b]

                // Find the interval containing 'a'
                auto it = connected.lower_bound(Interval{a, 0, false});
                if(it == connected.end() || it->start > a){
                    if(it == connected.begin()) {
                        // No interval contains 'a'
                        continue;
                    }
                    --it;
                }
                if(!(it->start <= a && it->end >= b)){
                    // The interval does not fully contain [a, b]; cannot split
                    continue;
                }

                // Remove the old interval and adjust invalid_count if necessary
                if(!it->is_valid){
                    invalid_count--;
                }
                connected.erase(it);

                // Split into two new intervals: [start, a] and [b, end]
                if(a >= it->start){
                    int start1 = it->start;
                    int end1 = a;
                    if(start1 <= end1){
                        int min_p1 = *min_element(p.begin()+start1-1, p.begin()+end1);
                        int max_p1 = *max_element(p.begin()+start1-1, p.begin()+end1);
                        bool is_valid1 = (min_p1 >= start1 && max_p1 <= end1);
                        connected.insert(Interval{start1, end1, is_valid1});
                        if(!is_valid1){
                            invalid_count++;
                        }
                    }
                }

                if(b <= it->end){
                    int start2 = b;
                    int end2 = it->end;
                    if(start2 <= end2){
                        int min_p2 = *min_element(p.begin()+start2-1, p.begin()+end2);
                        int max_p2 = *max_element(p.begin()+start2-1, p.begin()+end2);
                        bool is_valid2 = (min_p2 >= start2 && max_p2 <= end2);
                        connected.insert(Interval{start2, end2, is_valid2});
                        if(!is_valid2){
                            invalid_count++;
                        }
                    }
                }
            }
            // If the connection status hasn't changed, do nothing
        }

        // After processing the query, output the result
        cout << (invalid_count == 0 ? "YES" : "NO") << "\n";
    }

    return 0; // Ensure the function returns an integer
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL); // Fast I/O

    int tc;
    if(MT) cin >> tc; // Read number of test cases if MT is set
    else tc = 1; // Otherwise, assume a single test case

    while(tc--){
        solve(); // Execute the solve function for each test case
    }
    cout << endl;
    // No need for an additional newline at the end
}

