# Membaca assembly fungsi penjumlahan

Tampilkan instruksi fungsi `jumlah` dari [program latihan](README.md#siapkan-program-latihan). Opsi `-M intel` memilih sintaks Intel. Pada instruksi dua operan seperti `mov tujuan, sumber`, operan tujuan ditulis di kiri.

```sh
objdump -d -M intel --disassemble=jumlah latihan
```

## Ikuti perubahan nilai

Berikut potongan yang dapat dihasilkan GCC untuk `return kiri + kanan;`. Offset dan pilihan register bisa berbeda. Mulai dengan nilai `edi = 7` dan `esi = 5` saat fungsi dipanggil.

```asm
mov DWORD PTR [rbp-0x4], edi
mov DWORD PTR [rbp-0x8], esi
mov edx, DWORD PTR [rbp-0x4]
mov eax, DWORD PTR [rbp-0x8]
add eax, edx
```

1. Dua `mov` pertama menyimpan 7 dan 5 ke dua lokasi pada stack. Kurung siku berarti mengakses memori pada alamat hasil perhitungan. `DWORD PTR` menyatakan ukuran akses empat byte.
2. Dua `mov` berikutnya membaca nilai itu kembali. Kini `edx` berisi 7 dan `eax` berisi 5. `eax` adalah 32 bit terbawah `rax`. Menulis ke `eax` juga mengosongkan 32 bit teratas `rax`.
3. `add eax, edx` menulis 12 ke `eax`. Nilai `edx` tetap 7.

## Kenali batas fungsi

Pada awal fungsi, `push rbp` menyimpan nilai lama `rbp` di stack dan `mov rbp, rsp` menetapkan acuan untuk mengakses data lokal. `rsp` menunjuk puncak stack. Pada akhir contoh ini, `pop rbp` memulihkan nilai lama dan `ret` mengambil alamat kembali dari stack untuk melanjutkan eksekusi di pemanggil. Bentuk pembuka dan penutup fungsi dapat berubah sesuai opsi kompilasi.

**Latihan.** Baca instruksi dengan tujuan dan sumber tertukar di atas kertas. Apa beda `mov eax, [rbp-0x8]` dan `mov [rbp-0x8], eax`? Yang pertama memperbarui register, yang kedua memperbarui isi memori. Cari kedua arah perpindahan itu pada hasil `objdump` milikmu.

Untuk contoh perbandingan, lompatan bersyarat, dan perulangan, lihat [catatan assembly reverse engineering](../reverse/notes/re2-assembly.md).

[Lanjut ke konvensi pemanggilan](03-abi.md) · [Indeks PWN](README.md)
