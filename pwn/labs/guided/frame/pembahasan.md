# Pembahasan frame

Tiga frame kode latihan aktif: nilai → tagihan → main. Dua register argumen saat masuk ke nilai memuat 3 dan 4. Beralih frame dengan `up` mengubah konteks inspeksi, sementara proses tetap berhenti. `down` kembali memilih frame terdalam. Sesudah `finish` pertama, register hasil memuat 12. Variabel `subtotal` baru dapat dipercaya setelah instruksi penyimpanan hasil berjalan. Sesudah `finish` kedua, biaya tetap 2 sudah ditambahkan sehingga hasilnya 14.

[Kembali ke soal](README.md)
