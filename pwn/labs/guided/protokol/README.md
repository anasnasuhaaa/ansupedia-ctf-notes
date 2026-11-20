# Mengukur byte pada proses terpisah

**Tujuan.** Bedakan karakter, byte, dan pembatas baris. Siapkan Make, C compiler, Python dengan pwntools serta [demo dan kontrak pesannya](../../../templates/README.md). Lab membangun sumber demo yang sama secara lokal. Di shell dari direktori ini:

```sh
make
printf 'é\n' | ./demo
python3 ukur.py
make check
```

Sebelum membuka skrip, prediksi panjang untuk masukan kosong, satu spasi, satu karakter é dalam UTF-8 dan 32 huruf x. Gambarkan byte yang dibaca demo sampai newline. Periksa apakah percobaan kedua memerlukan proses baru. Berhasil bila keempat balasan cocok tepat, termasuk newline. [Pembahasan](pembahasan.md) · [Indeks lab](../../README.md)
