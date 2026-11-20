#include <stdio.h>

int main(void) {
    unsigned char data[2];
    if (fread(data, 1, sizeof data, stdin) != sizeof data ||
        getchar() != EOF || ferror(stdin)) {
        fputs("perlu tepat dua byte\n", stderr);
        return 2;
    }
    unsigned nilai = (unsigned)data[0] | ((unsigned)data[1] << 8);
    printf("%u\n", nilai);
    return 0;
}
