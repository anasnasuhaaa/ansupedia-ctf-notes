# Mengenal ELF Linux x86-64

Setelah mengompilasi [program latihan](README.md#siapkan-program-latihan), kamu memiliki berkas ELF (*Executable and Linkable Format*). Baca header untuk mengetahui bagaimana alat harus menafsirkan byte di dalamnya.

```sh
file latihan
readelf -hW latihan
```

| Kolom header | Cara membaca hasil |
| --- | --- |
| `Class` | `ELF64` menunjukkan format ELF 64-bit. |
| `Machine` | `X86-64` menunjukkan arsitektur instruksi program. |
| `Data` | *Little endian* berarti byte bernilai paling rendah disimpan pada alamat paling kecil. Bilangan 32-bit `0x12345678` tersimpan sebagai `78 56 34 12`. |
| `Type` | Biner latihan dapat bertipe `EXEC` atau `DYN`, tergantung konfigurasi GCC. Untuk `DYN`, periksa apakah `file` mengenalinya sebagai *PIE executable*. Pustaka bersama juga memakai tipe `DYN`. |
| `Entry point address` | Alamat awal eksekusi yang ditetapkan untuk berkas ini. Pada program C biasa, kode awal menyiapkan lingkungan sebelum memanggil `main`. |

## Dari berkas ke memori

```sh
readelf -SW latihan
readelf -lW latihan
```

Perintah pertama menampilkan *section*, yaitu pengelompokan isi berkas yang digunakan antara lain oleh linker dan debugger. Cari `.text` untuk instruksi mesin dan `.rodata` untuk data hanya-baca seperti teks format `printf`. Informasi debug dari opsi `-g` biasanya muncul di section seperti `.debug_info`.

Perintah kedua menampilkan *program header*. Entri `LOAD` menjelaskan segmen yang perlu dipetakan ke memori. `Offset` menyatakan posisi byte di berkas, sedangkan `VirtAddr` menyatakan alamat virtual segmen menurut ELF. Pada PIE, alamat saat dijalankan juga bergantung pada lokasi pemuatan.

**Latihan.** Cari `.text` di tabel *Section to Segment mapping* pada akhir keluaran. Gunakan nomor segmennya untuk menemukan baris yang sesuai di tabel *Program Headers* (nomor dimulai dari nol). Apa izin segmen itu? Pada hasil kompilasi biasa, kolom `Flg` berisi `R E`, sehingga instruksi dapat dibaca dan dijalankan.

[Rujukan perintah readelf dari GNU Binutils](https://sourceware.org/binutils/docs/binutils/readelf.html)

[Lanjut ke assembly](02-assembly.md) · [Indeks PWN](README.md)
