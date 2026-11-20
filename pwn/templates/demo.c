#include <stdio.h>
#include <stdlib.h>

static void lapor(size_t panjang) {
    printf("BYTE %zu\n", panjang);
}

int main(void) {
    size_t panjang = 0;
    fputs("teks> ", stdout);
    fflush(stdout);
    int ch;
    while ((ch = getchar()) != '\n') {
        if (ch == EOF || panjang == 32) {
            fputs("baris tidak lengkap atau terlalu panjang\n", stderr);
            return EXIT_FAILURE;
        }
        ++panjang;
    }
    lapor(panjang);
    return EXIT_SUCCESS;
}
