# Ketika program berhenti

Simpan perintah persis, stdin, stderr, status keluar dan hash biner. Di shell, `echo "$?"` segera setelah perintah program memberi status perintah terakhir. Pada pipeline shell biasa ini umumnya status tahap terakhir. Reproduksi pengamatan pada program yang kamu bangun sendiri dengan input normal yang sudah dicatat.

| Pengamatan | Periksa berikutnya | Koreksi atau cara membedakan |
| --- | --- | --- |
| Keluar 2 dengan pesan aplikasi | Baca kontrak argc atau panjang stdin | Uji input sah dan bandingkan; status aplikasi belum menunjukkan sinyal |
| SIGSEGV | Di (gdb) gunakan `bt`, `frame 0`, `x/i $pc`, `info locals` | Telusuri kepemilikan, batas dan inisialisasi objek sejak pemanggil; lokasi fault dapat berbeda dari akar kesalahan |
| SIGABRT | Periksa stderr dan frame aplikasi terdekat dengan `up` | Periksa assert yang gagal atau diagnostik allocator sebelum titik abort |
| EOF atau timeout pada Python | Amati `python3 solve.py DEBUG` di folder template | Cocokkan prompt, newline dan exit proses; bandingkan dengan input langsung di shell |
| Core terbuka tetapi simbol tidak cocok | Bandingkan build ID lewat `readelf -nW` pada berkas arsip build | Gunakan executable, pustaka dan simbol dari build yang merekam core |
| Langkah GDB tidak mengikuti sumber | Periksa optimasi dan informasi debug | Bangun salinan diagnosis dengan `-g -O0`; simpan identitas build asli untuk pembandingan |

Tulis satu dugaan yang dapat diuji, misalnya “input belum diakhiri newline”, lalu ulangi dengan satu perbedaan. Latih pembacaan snapshot tanpa crash lewat [latihan core](../05-debugging.md). [Kontrak memori](../06-keamanan-memori.md) · [Alur debugging](debugging-workflow.md)
