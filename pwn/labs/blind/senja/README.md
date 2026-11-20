# Senja

**Misi.** Tentukan aturan pengukuran satu argumen teks. Kamu memiliki biner lokal, 15 menit dan catatan [analisis statis](../../../04-pemeriksaan-biner.md). Siapkan compiler C, Make, Binutils dan Python 3. Dari direktori soal, di shell:

```sh
make
file program
./program 'a  b'
./program 'aaa'
objdump -d -M intel --disassemble=main program
```

Catat dua hipotesis yang cocok dengan contoh pertama. Rancang masukan yang membedakan keduanya, lalu temukan cabang yang mendukung kesimpulan. Periksa juga argumen kosong dan pemanggilan tanpa argumen. Tulis aturan prediksi, stdout, stderr dan status keluar untuk tiap kasus sebelum melihat jawaban.

Berhasil bila aturanmu dapat memprediksi kasus baru dan satu kondisi cabang dapat dijelaskan dari instruksi. Jalankan `make check` setelah menyimpan prediksi. [Buka pembahasan sesudah latihan](pembahasan/README.md) · [Indeks lab](../../README.md)
