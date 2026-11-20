# Pagi

**Misi.** Jelaskan format catatan dua byte yang dibaca dari stdin. Siapkan compiler C, Make, Python 3 dan Binutils. Gunakan [catatan urutan byte](../../../01-elf.md) jika perlu. Dari direktori soal, coba di shell:

```sh
make
printf '\001\002' | ./program
printf '\002\001' | ./program
printf '\001' | ./program
echo "$?"
```

Simpan hasil desimal dan status keluar. Ujilah dugaanmu pada masukan yang mengandung byte nol serta catatan yang disusul satu byte tambahan. Temukan instruksi atau ekspresi assembly yang menjelaskan bobot kedua posisi. Jatah waktu 15 menit; simpan catatan sebelum membuka sumber atau kasus uji.

Berhasil bila kamu dapat memprediksi satu pasangan baru dan menentukan kapan pesan dikirim ke stderr. Jalankan `make check` setelah selesai. [Buka pembahasan sesudah latihan](pembahasan/README.md) · [Indeks lab](../../README.md)
