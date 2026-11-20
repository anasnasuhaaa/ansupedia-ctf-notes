#include <stdio.h>

static int nilai(int unit, int tarif) {
    return unit * tarif;
}

static int tagihan(int unit, int tarif, int tetap) {
    int subtotal = nilai(unit, tarif);
    return subtotal + tetap;
}

int main(void) {
    printf("total=%d\n", tagihan(3, 4, 2));
    return 0;
}
