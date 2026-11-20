#include <stdio.h>

static unsigned jumlah(const unsigned char *awal, size_t banyak) {
    unsigned total = 0;
    for (size_t i = 0; i < banyak; ++i)
        total += awal[i];
    return total;
}

int main(void) {
    const unsigned char data[] = {2, 3, 5, 7};
    for (size_t pos = 0; pos <= sizeof data; ++pos) {
        size_t sisa = sizeof data - pos;
        printf("%zu %u\n", sisa, jumlah(data + pos, sisa));
    }
    return 0;
}
