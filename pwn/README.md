# Dasar PWN di Linux x86-64

Bagaimana pemanggilan `jumlah(7, 5)` di C terlihat di dalam berkas ELF? Di register mana kedua angka itu berada ketika fungsi mulai berjalan? Jalur ini memakai satu program kecil agar kamu bisa mencocokkan kode C, instruksi mesin, dan nilai yang terlihat di debugger.

## Siapkan program latihan

Gunakan terminal Linux x86-64 dengan GCC, `file`, GNU Binutils, dan GDB. Pwndbg bersifat opsional. Buat direktori latihan di luar repositori, lalu simpan kode berikut sebagai `latihan.c` di sana.

```c
#include <stdio.h>

int jumlah(int kiri, int kanan) {
    return kiri + kanan;
}

int main(void) {
    int hasil = jumlah(7, 5);
    printf("hasil = %d\n", hasil);
    return 0;
}
```

Dari direktori yang berisi `latihan.c`, kompilasi dan jalankan program.

```sh
gcc -g -O0 -fno-omit-frame-pointer -o latihan latihan.c
./latihan
```

Keluaran yang diharapkan adalah `hasil = 12`. Opsi `-g` menyertakan informasi untuk debugger, `-O0` memudahkan pencocokan instruksi dengan baris C, dan `-fno-omit-frame-pointer` memudahkan pengamatan bingkai fungsi. Jalankan perintah pada tiap modul dari direktori latihan ini.

[Kembali ke indeks repositori](../README.md)
