#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void generate_mountains(int k, int pos, ll num, int last_digit, int used_digits, int unique_middle_digit, int L, vector<ll>& mountains){
    if(pos == L){
        mountains.push_back(num);
        return;
    }
    if(pos < k +1){
        for(int d = last_digit; d <=9; d++){
            if(d ==0){
                continue;
            }
            if(pos ==k){
                if( (used_digits & (1<<d)) !=0 ){
                    continue;
                }
                generate_mountains(k, pos +1, num*10 +d, d, used_digits, d, L, mountains);
            }
            else{
                generate_mountains(k, pos +1, num*10 +d, d, used_digits | (1<<d), unique_middle_digit, L, mountains);
            }
        }
    }
    else{
        for(int d=1; d <= last_digit; d++){
            if(d == unique_middle_digit){
                continue;
            }
            generate_mountains(k, pos +1, num*10 +d, d, used_digits | (1<<d), unique_middle_digit, L, mountains);
        }
    }
}

int main(){
    freopen("cottontail_climb_part_2_input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<ll> mountains;

    for(int k=0; k<=9; k++){
        int L= 2*k +1;
        for(int d=1; d <=9; d++){
            if(k ==0){
                mountains.push_back( (ll)d );
                continue;
            }
            generate_mountains(k, 1, (ll)d, d, (1<<d), 0, L, mountains);
        }
    }

    sort(mountains.begin(), mountains.end());

    mountains.erase(unique(mountains.begin(), mountains.end()), mountains.end());

    int T;
    cin >> T;
    for(int tc=1; tc<=T; tc++){
        ll A, B, M;
        cin >> A >> B >> M;
        ll count=0;

        auto it_low = lower_bound(mountains.begin(), mountains.end(), A);
        auto it_up = upper_bound(mountains.begin(), mountains.end(), B);

        for(auto it = it_low; it != it_up; it++){
            if( (*it) % M ==0 ){
                count++;
            }
        }
        cout << "Case #" << tc << ": " << count << endl;
    }

    return 0;
}

