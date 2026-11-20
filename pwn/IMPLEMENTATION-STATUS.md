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

## Hasil akhir V2

Dua belas tahap selesai di cabang `main`. Tiga commit fondasi terdahulu menjadi titik awal. Tabel ini mencatat perubahan pada putaran lanjutan.

| Tahap | Commit | Hasil |
| --- | --- | --- |
| 01 | `378c818` | Audit riwayat, isi bab, dan kesenjangan awal |
| 02 | `7142f74` | Orientasi, jalur belajar dan navigasi |
| 03 | `ba87ca6` | Ukuran dan masa hidup objek C; penautan ELF |
| 04 | `0b7bf93` | Triage, cabang, source/sink dan navigasi Ghidra/IDA |
| 05 | `9a87d4f` | Stack dan mapping, core, checkpoint dan inspeksi ulang |
| 06 | `b2e192c` | Demo penghitung byte, pola conn/main dan tutorial pwntools |
| 07 | `1fce591` | Keluarga bug, koreksi, proteksi dan konsep runtime lanjut |
| 08 | `ded3c96` | Tiga lab terpandu beserta pembahasan dan pemeriksaan |
| 09 | `d6ec51e` | Dua lab mandiri beserta sumber dan jawaban terpisah |
| 10 | `ecf82dc` | Empat playbook, lima cheatsheet, glosarium, rujukan dan persiapan luring |
| 11 | `464f185` | Satu perintah uji semua lab, integrasi jalur baca dan pemeriksaan kualitas |
| 12 | Commit laporan ini | Rekap kasus, cakupan verifikasi dan batas pengujian |

### Pemeriksaan yang dijalankan

Lingkungan native Linux x86-64 menggunakan GCC 15.2.0, GNU Binutils 2.46, GDB sistem 17.1, glibc 2.43, Python 3.14.4 dan pwntools 4.15.0. Distribusi pwndbg 2026.09.15 memakai GDB 17.2 sendiri.

| Bagian | Perintah atau kasus | Hasil teramati |
| --- | --- | --- |
| Fondasi | Kompilasi dua blok C dari Markdown; file, nm, readelf, strings, objdump | Penjumlahan 12; variasi 9 dan 5 menghasilkan 14. Pada program objek: ELF ELF eLF; ukuran 4, 3 dan 8 |
| Analisis statis | Pemetaan string format ke .rodata, disassembly main/salin dan tabel relokasi | Ukuran salinan 4, jalur salin bersyarat setelah malloc; pada latihan jumlah ditemukan relokasi printf |
| Debugger | break di entri, register, stepi/nexti, finish, info frame; buat dan baca core; checkpoint/restart | Argumen 7/5 dan hasil 12; core menunjukkan jumlah dan main. Checkpoint mengembalikan posisi di main. GDB memperingatkan satu halaman memori gagal disalin ke core |
| Pwndbg | context regs/disasm, telescope dan vmmap di breakpoint | Register argumen, slot kembali, serta rentang kode dan stack terlihat |
| Template | Jalankan solve.py biasa, DEBUG dan GDB; uji packing dan unpacking | Balasan terurai 4 byte. GDB attach memakai peluncur terminal headless untuk tes dan mencetak panjang 4 pada breakpoint lapor |
| Batas demo | Kosong, UTF-8 é, tepat 32 byte, 33 byte, EOF tanpa newline | Tiga pertama diterima; dua terakhir menghasilkan status gagal dan pesan stderr |
| Memori dan proteksi | Build objek dengan ASan/UBSan, lalu build hardening tersendiri dan periksa dengan pwn checksec/readelf | Jalur normal selesai tanpa laporan sanitizer. Build hardening menunjukkan canary, NX, PIE, GNU_RELRO dan NOW |
| Irisan | 1 kasus stdout dengan lima irisan, termasuk panjang nol | Seluruh baris sesuai; pada breakpoint bersyarat, byte 5 dan 7 menghasilkan 12 |
| Frame | 1 kasus biaya bertingkat dan pemeriksaan GDB | Dua hasil saat kembali berturut-turut 12 dan 14 |
| Protokol | 4 proses untuk kosong, spasi, UTF-8 é dan 32 huruf | Balasan persis 0, 1, 2, 32 byte |
| Senja | 7 kasus argv, termasuk tanpa argumen, argumen berlebih serta spasi/tab | Status, stdout dan stderr sesuai seluruh kasus |
| Pagi | 9 kasus stdin biner, termasuk endian, nol, nilai maksimum dan panjang keliru | Status, stdout dan stderr sesuai seluruh kasus |

Dari akar repo, `make -BC pwn/labs check` mengulang 22 kasus di 5 lab. Build dan pengujian diulang dari ekspor Git bersih; template juga dibangun dan dijalankan terpisah. Dalam pemeriksaan tambahan dengan `strace` yang menolak syscall `connect`, seluruh rangkaian build lab, tes dan smoke test template berhasil tanpa panggilan `connect` tercatat.

Pemeriksaan Markdown meliputi README akar dan semua halaman PWN: 39 halaman terjangkau, tautan relatif beserta fragmen terselesaikan, pasangan pagar kode lengkap, dan 20 blok shell lolos `sh -n`. Tiga berkas Python PWN lolos `python3 -m compileall -q pwn`. Dump assembly bergantung pada build; angka alamat sengaja tidak digunakan sebagai kriteria lulus. Pemeriksaan Git mencakup `git diff --check` dan perbandingan direktori historis dengan commit awal.

### Batas verifikasi dan keadaan Git

Antarmuka Ghidra dan IDA serta contoh opsional patchelf tidak diuji secara interaktif. Panduan pemasangan paket/venv dan pemulihan dari wheelhouse tidak diuji pada mesin baru. Pembuatan dan verifikasi cadangan Git bundle telah diuji di direktori sementara.

Kedua prompt tetap di luar indeks. Putaran ini tidak menjalankan push atau mengubah remote. Ref pelacak lokal `origin/main` awalnya berada pada `8f5c363`; selama pengerjaan reflog mencatat `update by push` ke `9a87d4f`. Reflog tersebut tidak mengidentifikasi proses pemulanya.
