# Dasar PWN di Linux x86-64

[Mulai di sini](START-HERE.md) · [Labs](labs/README.md) · [Playbook 15 menit](playbook/first-15-minutes.md) · [Rujukan cepat](#rujukan-cepat-luring)

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

[Interaksi Python/pwntools](templates/README.md) — bangun penghitung byte lokal dan cocokkan balasannya dengan input.

Untuk meninjau program C, ikuti [kontrak memori](06-keamanan-memori.md), [proteksi runtime](07-proteksi.md), lalu [pengantar allocator dan batas proses](08-konsep-lanjut.md).

[Laboratorium lokal](labs/README.md) — soal, perintah build dan kriteria keberhasilan per latihan.

## Rujukan cepat luring

| Kebutuhan | Buka |
| --- | --- |
| Baru menerima biner latihan | [15 menit pertama](playbook/first-15-minutes.md) · [Perintah inspeksi](cheatsheets/commands.md) |
| Berhenti di fungsi atau membaca core | [Alur debugging](playbook/debugging-workflow.md) · [Diagnosis crash](playbook/crash-troubleshooting.md) · [pwndbg](cheatsheets/pwndbg.md) |
| Mencari arti register atau metadata | [Register dan ABI](cheatsheets/registers-and-abi.md) · [Matriks checksec](cheatsheets/checksec-matrix.md) |
| Menguji input/output | [Pwntools ringkas](cheatsheets/pwntools.md) · [Soal terpandu dan mandiri](labs/README.md) |
| Bersiap untuk final | [Setup](environment/setup.md) · [Checklist luring](environment/offline-checklist.md) · [Alur kompetisi](playbook/competition-workflow.md) |
| Mencari istilah dan bantuan alat | [Glosarium](references/glossary.md) · [Rujukan lokal](references/further-reading.md) |
