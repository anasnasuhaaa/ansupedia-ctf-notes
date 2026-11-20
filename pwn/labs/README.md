# Laboratorium lokal

Setiap latihan memakai direktori kerjanya sendiri. Jalankan perintah pada halaman soal dari direktori tersebut. `make check` memeriksa keluaran yang diharapkan dan gagal jika program tidak menuntaskan interaksi dalam batas waktu pembacaan.

| Terpandu | Bukti yang dikumpulkan |
| --- | --- |
| [Irisan](guided/irisan/README.md) | Dua elemen, satu pointer, dan batas iterasi kosong |
| [Frame](guided/frame/README.md) | Nilai argumen saat masuk dan hasil dua fungsi saat kembali |
| [Protokol](guided/protokol/README.md) | Empat balasan nyata dari empat proses lokal |

[Indeks PWN](../README.md) · [Jalur belajar](../LEARNING-PATH.md)

## Latihan mandiri

Pilih [Senja](blind/senja/README.md) atau [Pagi](blind/pagi/README.md). Buka README soal dan jalankan `make` tanpa membuka folder `pembahasan`. Setiap folder pembahasan menyimpan jawaban, sumber, dan kasus uji. Catat prediksi sebelum menjalankan `make check`.

Dari akar repo, `make -C pwn/labs check` membangun dan menguji kelima lab. Gunakan `make -BC pwn/labs check` untuk membangun ulang semuanya. Untuk menjaga soal mandiri tetap menjadi latihan tanpa bocoran, jalankan pemeriksaan menyeluruh setelah mengerjakan kedua soal: laporan tes menyebutkan nama kasus.
