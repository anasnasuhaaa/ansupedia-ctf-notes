# Pemeriksaan sebelum sesi luring

- [ ] Baca aturan acara dan simpan catatan yang diizinkan di direktori lokal. Coba buka indeks dan soal di editor ketika browser ditutup.
- [ ] Catat `git rev-parse --short HEAD`, versi compiler, Python, pwntools dan GDB. Untuk cadangan riwayat yang sudah di-commit, di akar repo jalankan `git bundle create ../catatan-pwn.bundle HEAD`, lalu `git bundle verify ../catatan-pwn.bundle`. Simpan catatan pribadi di luar Git secara terpisah; tentukan nama cadangan baru bila tujuan sudah ada.
- [ ] Pastikan venv dan compiler dapat digunakan tanpa mengunduh. Dari akar repo jalankan `make -C pwn/labs/guided/irisan -B check` dan `make -C pwn/labs/guided/protokol -B check` untuk memaksa build baru.
- [ ] Jalankan GDB pada build debug dan hentikan di fungsi yang dikenal. Di GDB gunakan `set debuginfod enabled off` sebelum `run`; konfirmasi bahwa simbol program sendiri tetap tersedia.
- [ ] Di folder template, jalankan `make demo` dan `python3 solve.py`. Buka bantuan pwntools dari [daftar rujukan lokal](../references/further-reading.md).
- [ ] Tutup AI dan akses jaringan selama simulasi. Pilih satu [soal mandiri](../labs/README.md), siapkan timer, catat input dan prediksi sebelum membuka pembahasan.

[Penyiapan mesin](setup.md) · [Alur kompetisi](../playbook/competition-workflow.md)
