#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BITSET_SET(A,i)   ( (A)[(i)>>3] |=  (1u << ((i)&7)) )
#define BITSET_GET(A,i)   ( ((A)[(i)>>3] >> ((i)&7)) & 1u )

int main() {
    int n;
    if (scanf("%d", &n) != 1 || n < 0) return 0;

    int N = n + 1;
    size_t bytes = (size_t)(N + 1 + 7) / 8;
    unsigned char *arr = (unsigned char *)calloc(bytes, 1);
    if (!arr) return 0;

    int ops = 0;
    for (int i = 1; i <= N; ++i) {
        if (!BITSET_GET(arr, i)) {
            ++ops;
            BITSET_SET(arr, i);
            if (i <= N / 2) BITSET_SET(arr, 2 * i);
            if (i <= N / 3) BITSET_SET(arr, 3 * i);
        }
    }

    printf("%d\n", ops);
    free(arr);
    return 0;
}


