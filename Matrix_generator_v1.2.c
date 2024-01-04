#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define WANT_THE_MATRIX
// #define WANT_THE_LINKAGE

int a[1000][1000];

int spaceNum(int n) {
    int ret = 1;
    while (n >= 10) ret++, n/=10;
    return ret;
}

int main() {
    int Msize;  // matrix size
    int Mnode;
    int nodeNum[1000];
    srand(time(NULL));
    printf("Input the amount of webpages you want:\n");
    scanf("%d", &Msize);
    printf("Input the maximum amount of nodes each node can point to:\n");
    scanf("%d", &Mnode);
    if (Mnode >= Msize) {
        printf("ERROR: the max nodes cannot exceed the matrix size\n");
        return 0;
    }
    for (int i = 0; i < Msize; i++) {
        for (int j = 0; j < Msize; j++) {
            a[i][j] = 0;
        }
    }
    // make the webpage link to webpages
    for (int i = 0; i < Msize; i++) {
        int num = (rand() % (Mnode - 1)) + 1;
        for (int j = 0; j < num;) {
            int link = rand() % Msize;
            if (a[i][link] == 0 && link != i) {
                a[i][link] = 1;
                j++;
            }
        }
        nodeNum[i] = num;
    }
#ifdef WANT_THE_LINKAGE
    // print the webpage link to which webpages
    for (int i = 0; i < Msize; i++) {
        printf("%d: ", i);
        for (int j = 0; j < Msize; j++) {
            if (a[i][j] == 1) {
                printf("%d ", j);
            }
        }
        printf("\n");
    }
#endif
#ifdef WANT_THE_MATRIX
    // print the matrix
    for (int j = 0; j < Msize; j++) {
        for (int i = 0; i < Msize; i++) {
            if (a[i][j] == 1 && nodeNum[i] == 1)
            {
                printf("1");
                for(int k = 0 ; k < spaceNum(nodeNum[i]) + 2; k++)
                {
                    printf(" ");
                }
            }
            else if (a[i][j] == 1)
                printf("1/%d ", nodeNum[i]);
            else {
                printf("0");
                for (int k = 0; k < spaceNum(nodeNum[i]) + 2; k++) {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
#endif
    return 0;
}