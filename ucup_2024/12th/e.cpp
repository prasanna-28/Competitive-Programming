#include <bits/stdc++.h>
using namespace std;

int ctinit(const string& s) {
    int count = 0;
    int n = s.length();
    for(int i = 0; i <= n - 4; ++i){
        if(s[i] == 'C' && s[i+1] == 'C' && s[i+2] == 'P' && s[i+3] == 'C'){
            count++;
        }
    }
    return count;
}

int compute(const string& s, int pos, char insert_char){
    int new_good = 0;
    for(int offset = -3; offset <= 0; ++offset){
        int window_start = pos + offset;
        if(window_start < 0 || window_start + 3 >= static_cast<int>(s.length()) + 1){
            continue;
        }
        string window = "";
        for(int j = 0; j < 4; ++j){
            int idx = window_start + j;
            char c;
            if(idx < pos){
                c = s[idx];
            }
            else if(idx == pos){
                c = insert_char;
            }
            else{
                c = s[idx - 1];
            }
            window += c;
        }
        if(window[0] == 'C' && window[1] == 'C' && window[2] == 'P' && window[3] == 'C'){
            new_good++;
        }
    }
    return new_good;
}

int run(int n, const string& s){
    int initial_count = ctinit(s);
    int max_final = initial_count;
    for(int pos = 0; pos <= n; ++pos){
        for(char insert_char : {'C', 'P'}){
            int gain = compute(s, pos, insert_char);
            int final_value = initial_count + gain;
            if(final_value > max_final){
                max_final = final_value;
            }
        }
    }
    return max_final;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    vector<int> results;
    while(T--){
        int n;
        string s;
        cin >> n >> s;
        if(s.length() != static_cast<size_t>(n)){
            while(static_cast<int>(s.length()) < n){
                char c;
                cin >> c;
                s += c;
            }
            if(static_cast<int>(s.length()) > n){
                s = s.substr(0, n);
            }
        }
        int result = run(n, s);
        results.push_back(result);
    }
    for(auto res : results){
        cout << res << "\n";
    }
    cout<<endl;
    return 0;
}

