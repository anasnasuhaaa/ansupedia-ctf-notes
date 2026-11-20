# Pemeriksaan awal biner

Bayangkan kamu hanya memegang berkas `latihan` hasil [kompilasi sebelumnya](README.md#siapkan-program-latihan). Apa yang bisa kamu pelajari tanpa menjalankan program? Mulailah dari pertanyaan yang bisa dijawab oleh setiap alat.

| Pertanyaan | Perintah | Bukti yang dicari |
| --- | --- | --- |
| Untuk mesin apa program dibuat? | `file latihan` | Ringkasan format, arsitektur, dan cara penautan. Cocokkan dengan kolom `Machine` pada `readelf -hW latihan`. |
| Pustaka apa yang diminta? | `readelf -dW latihan` | Entri `NEEDED` mencatat dependensi langsung. Pada kompilasi dinamis biasa, salah satunya adalah `libc.so.6`. |
| Fungsi apa yang dapat ditemukan berdasarkan nama? | `nm -n latihan` | Cari `T jumlah` dan `T main`. Huruf `T` menandai simbol global yang didefinisikan di bagian kode. Opsi `-n` mengurutkan simbol menurut alamat. |
| Teks apa yang tersimpan? | `strings -a latihan` | Cari `hasil = %d`. Deretan karakter ini memberi petunjuk tentang format keluaran. |
| Bagaimana fungsi-fungsi itu berhubungan? | `objdump -d -M intel --disassemble=main latihan` | Cari pemanggilan `jumlah`, lalu pemanggilan `printf`. Hubungkan nama simbol tadi dengan urutan instruksi di `main`. |

**Latihan.** Jelaskan mengapa `strings` menemukan `hasil = %d`, sedangkan saat dijalankan program mencetak `hasil = 12`. Berkas menyimpan teks format. Saat program berjalan, `printf` mengganti `%d` dengan nilai integer yang diterimanya. Untuk membuktikan nilai itu, ikuti register hasil di modul berikutnya.

Jika `nm` melaporkan `no symbols`, periksa kembali berkas yang kamu pilih. Proses *stripping* dapat membuang tabel simbol biasa sehingga nama fungsi lokal sulit dicari. Untuk mengikuti latihan berdasarkan nama `jumlah`, gunakan biner yang dikompilasi dari contoh pada indeks PWN.

[Lanjut ke debugging](05-debugging.md) · [Indeks PWN](README.md)
