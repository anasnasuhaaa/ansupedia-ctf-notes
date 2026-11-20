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

## Urutan belajar

1. [ELF Linux x86-64](01-elf.md) — temukan bagian berkas yang berisi instruksi dan lihat cara Linux memetakannya ke memori.
2. [Membaca assembly](02-assembly.md) — ikuti dua bilangan dari register hingga menjadi hasil penjumlahan.
3. [Pemanggilan fungsi menurut System V AMD64](03-abi.md) — cocokkan argumen dan nilai balik C dengan register di batas pemanggilan.
4. [Pemeriksaan awal biner](04-pemeriksaan-biner.md) — susun profil program dari header, simbol, pustaka, dan teks yang tersimpan.
5. [Debugging dengan GDB dan pwndbg](05-debugging.md) — hentikan program saat fungsi dimasuki dan periksa hasil saat fungsi kembali.

[Kembali ke indeks repositori](../README.md)

## Belajar mandiri

[Mulai di sini](START-HERE.md) · [Jalur belajar](LEARNING-PATH.md) · [Status dan hasil verifikasi](IMPLEMENTATION-STATUS.md)

Jika baru belajar C, mulai dari [objek, pointer, dan masa hidup](00-memori-c.md) sebelum membaca ELF.
