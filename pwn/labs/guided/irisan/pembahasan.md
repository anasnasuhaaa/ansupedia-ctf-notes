# Pembahasan irisan

Saat pos bernilai 2, pointer menunjuk elemen ketiga, yaitu 5. Dua byte yang sah dibaca bernilai 5 dan 7; `finish` mengembalikan 12. Pada pos 4 pointer menunjuk satu posisi setelah array. Aturan C mengizinkan pembentukan pointer ini, tetapi melarang dereferensi di sana. Kondisi `i < banyak` langsung salah. `sizeof data` kebetulan sama dengan jumlah elemen karena tiap elemen berukuran satu byte. Bila tipe elemen berubah, gunakan `sizeof data / sizeof data[0]` untuk menghitung elemen.

[Kembali ke soal](README.md)
