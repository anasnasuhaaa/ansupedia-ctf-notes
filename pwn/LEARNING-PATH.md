# Jalur belajar Linux x86-64

Mulailah dari baris pertama yang belum bisa kamu buktikan di terminal. Simpan satu catatan pendek untuk tiap baris.

| Pertanyaan | Prasyarat dan bacaan | Bukti siap lanjut |
| --- | --- | --- |
| Apa yang benar-benar dijalankan? | Terminal dan [contoh kompilasi](README.md#siapkan-program-latihan) | Bangun ulang, catat keluaran untuk dua pasangan argumen |
| Di mana instruksi berada? | Biner latihan dan [ELF](01-elf.md) | Cocokkan section kode dengan satu segmen dan izinnya |
| Bagaimana nilai berpindah? | [Assembly](02-assembly.md), lalu [ABI](03-abi.md) | Tunjukkan sumber, tujuan, serta lebar operan pada satu instruksi |
| Apa yang bisa diketahui sebelum eksekusi? | [Pemeriksaan biner](04-pemeriksaan-biner.md) | Tulis satu fakta dari simbol dan satu hipotesis dari string |
| Kapan hasil pertama kali terlihat? | Call site dan [GDB](05-debugging.md) | Bandingkan dua register saat masuk dengan register hasil saat kembali |
| Byte mana yang boleh dibaca? | [Memori C](00-memori-c.md), [review kontrak](06-keamanan-memori.md) | Jelaskan baris terakhir pada [lab irisan](labs/guided/irisan/README.md) |
| Bagaimana loader dan runtime membatasi proses? | [Proteksi](07-proteksi.md) dan [konsep lanjut](08-konsep-lanjut.md) | Pisahkan satu properti berkas dari satu pengamatan proses hidup |
| Kapan balasan proses lengkap? | [Template Python](templates/README.md) dan [lab protokol](labs/guided/protokol/README.md) | Prediksi balasan UTF-8 dan bedakan EOF dari timeout |
| Dapatkah pengamatan diulang tanpa petunjuk? | [Soal mandiri](labs/README.md) dan [alur kompetisi](playbook/competition-workflow.md) | Jelaskan satu kasus baru sebelum membukanya di pembahasan |

Ulangi setiap pekan dengan satu perubahan terkontrol, misalnya nilai argumen atau tingkat optimasi. Pemula dapat menjelaskan hasil pada satu build; pembaca tingkat menengah dapat menemukan bukti setara ketika alamat dan susunan instruksi berubah. Untuk menilai kesiapan lomba, beri batas waktu, mulai dari direktori kosong dengan catatan lokal, dan minta diri sendiri menjelaskan satu dugaan yang gugur serta pengamatan yang menggugurkannya.

[Mulai di sini](START-HERE.md) · [Indeks PWN](README.md)
