# Pemeriksaan awal biner

Bayangkan kamu hanya memegang berkas `latihan` hasil [kompilasi sebelumnya](README.md#siapkan-program-latihan). Apa yang bisa kamu pelajari tanpa menjalankan program? Mulailah dari pertanyaan yang bisa dijawab oleh setiap alat.

| Pertanyaan | Perintah | Bukti yang dicari |
| --- | --- | --- |
| Untuk mesin apa program dibuat? | `file latihan` | Ringkasan format, arsitektur, dan cara penautan. Cocokkan dengan kolom `Machine` pada `readelf -hW latihan`. |
| Pustaka apa yang diminta? | `readelf -dW latihan` | Entri `NEEDED` mencatat dependensi langsung. Pada kompilasi dinamis biasa, salah satunya adalah `libc.so.6`. |
| Fungsi apa yang dapat ditemukan berdasarkan nama? | `nm -n latihan` | Cari `T jumlah` dan `T main`. Huruf `T` menandai simbol global yang didefinisikan di bagian kode. Opsi `-n` mengurutkan simbol menurut alamat. |
| Teks apa yang tersimpan? | `strings -a latihan` | Cari `hasil = %d`. Deretan karakter ini memberi petunjuk tentang format keluaran. |
| Bagaimana fungsi-fungsi itu berhubungan? | `objdump -d -M intel --disassemble=main latihan` | Cari pemanggilan `jumlah`, lalu pemanggilan `printf`. Hubungkan nama simbol tadi dengan urutan instruksi di `main`. |

**Latihan.** Jelaskan mengapa `strings` menemukan `hasil = %d`, sedangkan saat dijalankan program mencetak `hasil = 12`. Berkas menyimpan teks format. Saat program berjalan, `printf` mengganti `%d` dengan nilai integer yang diterimanya. Untuk membuktikan nilai itu, ikuti register hasil di modul berikutnya.

Jika `nm` melaporkan `no symbols`, periksa kembali berkas yang kamu pilih. Proses *stripping* dapat membuang tabel simbol biasa sehingga nama fungsi lokal sulit dicari. Untuk mengikuti latihan berdasarkan nama `jumlah`, gunakan biner yang dikompilasi dari contoh pada indeks PWN.

[Lanjut ke debugging](05-debugging.md) · [Indeks PWN](README.md)

## Dari string ke aliran data

**Tujuan.** Temukan satu lintasan dari sumber data ke fungsi yang memakainya dan nyatakan syarat agar lintasan itu diambil. Gunakan `objek` dari [latihan memori C](00-memori-c.md). Catat asal berkas dan hash untuk mengenali build yang sama; hash saja tidak membuktikan bahwa berkas layak dijalankan. Untuk berkas asing, awali dengan pembacaan statis di lingkungan analisis terpisah. Semua percobaan eksekusi di buku memakai program yang dibangun sendiri.

Di shell, dari direktori yang berisi `objek.c` dan biner debug:

```sh
sha256sum objek
strings -a -t x objek
nm -D objek
readelf -p .rodata objek
objdump -d -S -M intel --disassemble=salin objek
objdump -d -M intel --disassemble=main objek
```

1. Pilih string `array=%zu`. Offset dari `strings -t x` dihitung dari awal berkas. Alamat pada listing disassembly berada di ruang alamat virtual ELF. Cocokkan melalui section atau referensi silang sebelum menyamakan keduanya.
2. Ikuti awal data (*source*) dari array lokal di `main`: argumen kedua ke `salin` membawa kapasitas array. Di `salin`, periksa apakah nilai itu dipakai sebagai ukuran alokasi dan sebagai argumen ketiga `memcpy` (*sink*, titik penggunaan).
3. Tandai dua penerus cabang sesudah `malloc`. Bila hasil nol, fungsi melewati penyalinan; pemanggil memeriksa pointer sebelum menulis satu karakter. Tuliskan kedua syarat itu pada gambar alurmu. Nama impor saja belum menjelaskan ukuran buffer atau nilai yang mencapai panggilan.
4. Cocokkan satu baris C dengan instruksi melalui `-S`. Jika sumber tidak muncul, pastikan path sumber dapat dibaca dan build memakai `-g`. Jika panggilan hilang akibat inlining, bandingkan dengan build `-O0`.

### Dengan antarmuka grafis

Di **Ghidra**, buat proyek lokal *Non-Shared*, impor ELF dan periksa bahasa x86 little-endian 64-bit. Buka di CodeBrowser dan jalankan auto-analysis. Dari *Defined Strings*, buka string format di Listing, lalu ikuti referensi ke instruksi pemakainya. Di *Symbol Tree → Functions*, pilih `salin`; cocokkan kondisi pada Decompiler dengan dua jalur di *Function Graph*. Simpan komentar tentang ukuran salinan di call site. [Panduan Ghidra](https://ghidra.re/ghidra_docs/GhidraClass/Beginner/Introduction_to_Ghidra_Student_Guide.html)

Di **IDA**, buka salinan biner sebagai ELF dan tunggu analisis awal. Di *Strings* pilih format keluaran, lompat ke lokasinya, lalu gunakan `X` untuk melihat xref. Catat fungsi yang merujuk format itu. Buka `salin` dari *Functions*, gunakan tampilan graph dan telusuri kedua cabang ke titik kembali. Koreksi nama/tipe lokal hanya sejauh didukung instruksi dan ABI. Pseudocode adalah rekonstruksi; simpan instruksi pendukung bila tipe hasil dekompilasi meragukan. [Navigasi IDA di repositori](../reverse/notes/RE-03-IDA.md)

**Uji diri.** Data apa yang membuktikan kapasitas tujuan pada contoh ini? Apakah format teks di berkas membuktikan `printf` telah dipanggil? Ringkas kesimpulan dalam tiga kolom: fakta statis, dugaan tentang eksekusi, dan pengamatan runtime untuk mengujinya.

[Lanjutkan pengamatan di debugger](05-debugging.md)
