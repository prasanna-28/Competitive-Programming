#include <stdio.h>
#include <string.h>
#include <limits.h>

long long cache[5002][5002];
long long freq[5002];

void sol(long long (*dp)(long long, long long))
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        long long n;
        scanf("%lld", &n);
        for (int i = 0; i <= n; i++)
            memset(cache[i], -1, (n + 1) * sizeof(long long));

        for (int i = 0; i < n; i++)
        {
            long long x;
            scanf("%lld", &x);
            freq[x]++;
        }

        long long ans = n;
        for (long long i = n; i >= 0; i--)
        {
            if (dp(n, i) != LLONG_MIN)
                ans = i;
        }

        printf("%lld\n", ans);
        memset(freq, 0, (n + 1) * sizeof(long long));
    }
}

long long dp(long long idx, long long up)
{
    if (up < 0) return LLONG_MIN;
    if (idx == 0 && up == 0) return 0;
    if (idx == 0) return LLONG_MIN;
    if (cache[idx][up] != -1) return cache[idx][up];

    if (freq[idx])
        cache[idx][up] = dp(idx - 1, up - 1);
    else
        cache[idx][up] = dp(idx - 1, up);

    long long previous = dp(idx - 1, up);
    if (previous != LLONG_MIN)
    {
        long long potential = previous + freq[idx];
        if (potential <= up)
        {
            if (cache[idx][up] == LLONG_MIN || potential < cache[idx][up])
                cache[idx][up] = potential;
        }
    }
    return cache[idx][up];
}

int main()
{
    sol(dp);
    return 0;
}
