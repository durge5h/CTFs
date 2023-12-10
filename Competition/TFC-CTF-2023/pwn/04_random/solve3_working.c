#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    srand((unsigned int)time(0x0));
    for (int i = 0; i < 10; i++) {
        printf("%d ", rand());
    }
    printf("\n");
    printf("%s\n", argv[1]);
    return 0;
}
