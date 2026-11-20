# Lima belas menit pertama dengan ELF

Gunakan biner `latihan` yang dibangun dari [indeks PWN](../README.md#siapkan-program-latihan). Untuk berkas lain, catat asal dan tentukan apakah eksekusi layak dilakukan. Tahap awal dapat dikerjakan seluruhnya lewat inspeksi berkas.

| Menit | Di shell | Yang ditulis di catatan |
| --- | --- | --- |
| 0–3 | `sha256sum latihan`, `file latihan`, `readelf -hW latihan` | Identitas build, kelas ELF, mesin, endian dan tipe |
| 3–6 | `readelf -lW latihan`, `readelf -dW latihan` | Interpreter, izin LOAD dan dependensi langsung |
| 6–9 | `nm -n latihan`, `nm -D latihan`, `strings -a latihan` | Pilih satu simbol dan satu string untuk diperiksa |
| 9–12 | `objdump -d -M intel --disassemble=main latihan` | Call site yang dapat menjelaskan keluaran |
| 12–15 | Pada biner buatan sendiri, `./latihan`, lalu `gdb -q ./latihan` | Prediksi dan satu hasil yang bisa menggugurkannya |

Contoh catatan sebelum menjalankan: “Ada format bilangan desimal. Saya menduga nilainya hasil fungsi jumlah. Jika register hasil saat fungsi kembali berbeda dari angka yang dicetak, saya perlu memeriksa pemrosesan setelah call.” Bila simbol lokal tidak tersedia, gunakan string, impor dan referensi pada listing untuk memilih bagian yang layak dibaca.

[Inspeksi statis](../04-pemeriksaan-biner.md) · [Langkah debugger](debugging-workflow.md) · [Matriks proteksi](../cheatsheets/checksec-matrix.md)
