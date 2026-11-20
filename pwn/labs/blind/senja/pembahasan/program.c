#include <stdbool.h>
#include <stdio.h>

static size_t ukur(const char *teks) {
    size_t total = 0;
    bool aktif = false;
    for (; *teks; ++teks) {
        bool isi = *teks != ' ' && *teks != '\t';
        if (isi && !aktif)
            ++total;
        aktif = isi;
    }
    return total;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fputs("perlu satu argumen\n", stderr);
        return 2;
    }
    printf("%zu\n", ukur(argv[1]));
    return 0;
}
