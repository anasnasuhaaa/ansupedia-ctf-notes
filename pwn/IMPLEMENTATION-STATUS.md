# Status implementasi handbook PWN

## Titik awal

Audit pada cabang `main` dengan `git status --short --branch`, `git log -8 --oneline`, `git log -3 --stat`, dan `git ls-files -co --exclude-standard`. Dua berkas instruksi berada di luar indeks Git. Direktori reverse dan web sudah punya catatan sendiri.

| Commit terdahulu | Isi yang diperiksa | Keputusan |
| --- | --- | --- |
| 0fd5ce4 | Indeks, sumber C penjumlahan, perintah kompilasi | Pakai kembali sebagai contoh lintas bab |
| 19c204e | Section/segmen, register, call site, alignment, fungsi jumlah | Pertahankan urutan; lengkapi C, lifetime dan penautan |
| 1d06379 | Tabel inspeksi dan sesi GDB argumen/hasil | Perluas dengan penelusuran data, peta memori, core dan checkpoint |

Contoh di indeks dikompilasi dari blok C dengan GCC pada Linux x86-64 dan menghasilkan `hasil = 12`. Saat audit belum ada template Python, sumber lab terpisah, panduan penggunaan luring, playbook, atau cheatsheet PWN.

## Rencana pemeriksaan per tahap

| Tahap | Hasil yang dituju | Cara memeriksa |
| --- | --- | --- |
| 01–02 | Audit, titik mulai dan jalur belajar | Cocokkan riwayat dan tujuan tautan |
| 03–05 | C dan ELF, analisis statis, GDB/pwndbg | Kompilasi contoh, periksa objek dan ikuti nilai di debugger |
| 06–07 | Interaksi proses lokal, keamanan memori dan proteksi | Cocokkan balasan byte dan metadata ELF |
| 08–09 | Lab terpandu dan lab mandiri | Bangun dari sumber dan uji masukan serta status keluar |
| 10–11 | Referensi cepat, lingkungan, integrasi | Ulangi pengujian dari salinan bersih; cek tautan, fragmen dan blok kode |
| 12 | Status akhir | Catat kasus yang dijalankan dan batas verifikasi |

[Kembali ke indeks PWN](README.md)
