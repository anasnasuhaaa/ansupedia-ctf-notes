# Konvensi pemanggilan System V AMD64

Di Linux x86-64, fungsi C biasa mengikuti aturan *Application Binary Interface* (ABI) agar pemanggil dan fungsi yang dipanggil sepakat tentang tempat argumen dan hasil. Kita bisa menguji aturan itu di kedua sisi pemanggilan `jumlah(7, 5)` pada [program latihan](README.md#siapkan-program-latihan).

| Nilai pada batas pemanggilan | Lokasi menurut ABI |
| --- | --- |
| Enam argumen pertama bertipe integer atau pointer sederhana | Berurutan di `rdi`, `rsi`, `rdx`, `rcx`, `r8`, dan `r9`. Untuk `int` 32-bit, baca `edi`, `esi`, `edx`, `ecx`, `r8d`, dan `r9d`. |
| Argumen integer sederhana berikutnya | Pemanggil menyediakan ruang di stack. |
| Nilai balik bertipe `int` | Pemanggil membacanya dari `eax`. Untuk pointer 64-bit, gunakan `rax`. |

Argumen pecahan seperti `double` memakai aturan register XMM tersendiri. Tabel di atas cukup untuk kedua parameter `int` milik `jumlah`.

## Periksa dari sisi pemanggil

```sh
objdump -d -M intel --disassemble=main latihan
```

Temukan `call` dengan tujuan `<jumlah>`. Baca mundur beberapa instruksi dan cari nilai terakhir yang ditulis ke `edi` dan `esi`. GCC dapat mengisi `esi` lebih dahulu. Posisi parameter ditentukan oleh nama register, sehingga `edi = 7` tetap berarti `kiri = 7`. Setelah `call`, cari pemakaian pertama `eax` di `main`. Pada kompilasi latihan, hasilnya biasanya disalin ke variabel lokal `hasil`.

## Apa yang berubah selama pemanggilan?

Sebelum `call` pada contoh ini, pemanggil menyiapkan `rsp` pada batas 16 byte. Instruksi `call` menyimpan alamat instruksi berikutnya ke stack. Saat fungsi baru mulai, `rsp` turun 8 byte sehingga `rsp + 8` merupakan kelipatan 16. Ketika fungsi selesai, `ret` memakai alamat tadi untuk kembali ke pemanggil.

Jika fungsi memakai `rbx`, `rbp`, atau `r12` sampai `r15`, fungsi wajib memulihkan nilai register itu sebelum kembali. Pemanggil mengantisipasi bahwa register seperti `rax`, `rdi`, dan `rsi` dapat berubah. Karena itu, waktu yang tepat untuk membaca argumen adalah saat fungsi baru dimasuki.

**Latihan.** Jika baris C menjadi `jumlah(5, 7)`, prediksi nilai `edi`, `esi`, dan nilai baliknya. Jawabannya berturut-turut 5, 7, dan 12. Pertukaran ini terlihat pada register argumen meskipun program mencetak angka yang sama.

[Spesifikasi System V AMD64 dari proyek x86-64 psABI](https://gitlab.com/x86-psABIs/x86-64-ABI)

[Indeks PWN](README.md)
