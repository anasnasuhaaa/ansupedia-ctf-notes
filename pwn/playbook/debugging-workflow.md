# Menguji satu hipotesis di debugger

1. Simpan build, input, keluaran yang diharapkan dan pengamatan yang akan membedakan dua penjelasan. Untuk contoh jumlah: apakah perbedaan nilai muncul saat masuk fungsi, atau setelah kembali?
2. Di shell jalankan `gdb -q ./latihan`. Di **(gdb)**, `break *jumlah`, `run`, `info registers edi esi`. Tulis argumen pada batas fungsi.
3. Gunakan `x/i $pc` untuk instruksi berikut dan `bt` untuk pemanggilnya. Bila ingin membaca variabel lokal, melangkahlah sampai inisialisasinya selesai. Pilih `stepi` untuk masuk panggilan atau `nexti` untuk melewatinya.
4. Jalankan `finish`, baca `print/d $eax` sebelum instruksi pemanggil berikutnya. Lanjutkan dengan `continue` dan cocokkan angka dengan stdout.
5. Ganti tepat satu kondisi, bangun ulang jika sumber berubah, ulangi di sesi baru. Catat prediksi yang gugur dan titik pertama yang menunjukkan perbedaan.

Jika breakpoint tidak tercapai, cek nama berkas dengan `info files`, daftar breakpoint dengan `info breakpoints`, dan apakah cabang benar-benar ditempuh. [Bab GDB](../05-debugging.md) · [Jika proses berhenti](crash-troubleshooting.md)
