# Meninjau kontrak memori di C

**Tujuan.** Untuk setiap akses, tentukan objek, rentang byte yang sah, dan pemiliknya. Gunakan [program objek](00-memori-c.md) sebagai contoh yang dapat dikompilasi. *Undefined behavior* berarti standar C tidak menjamin hasil operasi itu. Crash bisa muncul jauh sesudah pelanggaran pertama atau program bisa selesai dengan keluaran keliru.

| Keluarga | Akar masalah dan petunjuk saat review | Gejala yang mungkin | Koreksi yang dapat diperiksa |
| --- | --- | --- | --- |
| Baca di luar batas | Indeks mencapai panjang; fungsi string menerima data tanpa terminator | Nilai tambahan, keluaran acak, atau fault | Simpan panjang aktual, periksa indeks sebelum membaca, batasi data biner dengan panjang |
| Tulis di luar batas | Perhitungan jumlah byte mengabaikan sisa kapasitas atau ruang terminator | Objek tetangga berubah; pemeriksaan memori gagal | Validasi kapasitas tujuan, sisakan satu byte untuk nol pada string |
| Buffer lokal meluap | Tujuan salinan berupa array otomatis dan panjang melebihi kapasitasnya | Hasil lokal berubah atau runtime menghentikan fungsi | Gunakan ukuran array di lingkup yang mengetahui ukurannya, tangani input parsial |
| Stack habis | Rekursi tanpa batas efektif atau frame lokal terlalu besar | Backtrace dalam atau kegagalan saat masuk fungsi | Batasi kedalaman, gunakan iterasi, periksa ukuran penyimpanan besar |
| Format string | Teks dari luar digunakan sebagai parameter format | Tanda persen mengubah interpretasi argumen, keluaran keliru atau fault | Untuk teks berterminator pilih `printf("%s", teks)` atau `fputs(teks, stdout)` |
| Use-after-free | Alias tetap dipakai sesudah pemilik melepas alokasi | Hasil berbeda antar-run, laporan allocator atau sanitizer | Tetapkan pemilik; batasi peminjaman hingga sebelum pelepasan |
| Double free | Jalur normal dan jalur gagal sama-sama melepas objek | Program bisa berhenti di allocator | Gabungkan cleanup, transfer kepemilikan secara eksplisit; mengosongkan satu pointer tidak memperbarui alias |
| Integer overflow | Jumlah elemen dikalikan ukuran sebelum dicek | Alokasi terlalu kecil atau hitungan keliru | Periksa batas **sebelum** perkalian; konversi masukan bertanda setelah rentangnya valid |

Overflow integer bertanda pada penjumlahan/perkalian biasa merupakan undefined behavior. Aritmetika unsigned mengikuti modulo, sehingga hasil terbungkus bisa sah sebagai angka C namun keliru sebagai ukuran. Sebelum menghitung `n * sizeof *items` untuk pointer elemen lengkap, uji `n > SIZE_MAX / sizeof *items` (ambil `SIZE_MAX` dari `<stdint.h>`). Pisahkan kebijakan untuk nol elemen dan kegagalan `malloc`.

**Contoh review.** Untuk menyalin `jumlah` byte ke buffer berkapasitas `kapasitas` mulai dari `posisi`, uji dahulu `posisi <= kapasitas`, lalu `jumlah <= kapasitas - posisi`. Pengurangan setelah pemeriksaan pertama aman untuk `size_t`. Jika kapasitas 8 dan posisi 6, tersisa 2 byte. Untuk salinan nonkosong, periksa juga bahwa sumber menyediakan semua byte tersebut. Untuk membuat string, hitung ruang terminator secara terpisah.

Di shell, kompilasi ulang contoh C lengkap dari bab objek dengan pemeriksaan tambahan:

```sh
gcc -std=c17 -Wall -Wextra -Wformat=2 -g -O1 -fno-omit-frame-pointer -fsanitize=address,undefined objek.c -o objek-cek
./objek-cek
```

Harapkan keluaran yang sama dengan contoh awal. ASan menginstrumentasi banyak akses memori, UBSan menguji sejumlah operasi yang melanggar aturan bahasa. Keduanya mengamati jalur yang dieksekusi. Saat membaca diagnostik, catat operasi pertama yang dilaporkan, stack pemanggilan dan asal alokasi bila tersedia. Hilangnya pesan pada satu input hanya memberi bukti untuk jalur itu.

**Uji diri.** Mengapa syarat `jumlah <= kapasitas - posisi` perlu didahului cek posisi? Di fungsi `salin`, siapa berhak melepas hasil saat berhasil? Bagaimana memastikan salinan dapat dilewati fungsi string?

[Proteksi runtime](07-proteksi.md) · [Indeks PWN](README.md)
