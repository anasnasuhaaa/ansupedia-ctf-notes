# Mulai di sini

Sediakan terminal Linux x86-64, editor, GCC dan Binutils. GDB dipakai setelah kamu bisa menemukan fungsi di berkas. Python dan pwntools diperlukan untuk latihan interaksi proses. Semua jalur relatif di indeks berangkat dari halaman yang sedang dibaca.

1. Buka [contoh jumlah](README.md#siapkan-program-latihan), salin sumber ke direktori kerja kosong, lalu ikuti perintah kompilasinya. Simpan perintah, versi GCC dan keluaran program.
2. Prediksi hasil bila argumen pertama diubah dari 7 menjadi 9. Bangun ulang setelah mengedit sumber, jalankan, lalu kembalikan contoh di direktori latihanmu ke bentuk awal sebelum mengikuti bab berikutnya.
3. Buka [bab ELF](01-elf.md) berdampingan dengan terminal. Temukan jenis mesin dan izin segmen kode pada **berkas yang baru kamu bangun**.
4. Di [bab GDB](05-debugging.md), hentikan proses di awal fungsi. Salin nama fungsi dan nilai argumen ke catatan. Gunakan nama simbol saat mengulang di proses baru.

Satu sesi mandiri cukup membahas satu pertanyaan. Contoh catatan: “Saya memperkirakan nilai 12 di `eax` setelah `finish`. Saya akan mengulang dengan argumen 9 dan 5 untuk memeriksa kapan register berubah.” Sisakan tempat untuk hasil aktual dan alasan bila prediksi meleset.

Untuk latihan tanpa AI, tutup percakapan dan browser, bangun ulang dari sumber lokal, lalu jelaskan kembali dua pengamatan tanpa melihat jawaban. Simpan pertanyaan yang belum terjawab sebagai awal sesi berikutnya.

[Jalur belajar dan ukuran kemajuan](LEARNING-PATH.md) · [Indeks PWN](README.md)

Untuk menyiapkan alat sebelum koneksi ditutup, ikuti [setup Linux](environment/setup.md). Setelah memahami `jumlah`, lanjutkan ke [lab frame](labs/guided/frame/README.md), lalu coba [satu soal mandiri](labs/README.md) memakai [playbook 15 menit](playbook/first-15-minutes.md).
