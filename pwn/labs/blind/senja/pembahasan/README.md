# Pembahasan Senja

`aaa` dan `a` sama-sama menghasilkan 1. Yang dihitung adalah awal rentang byte selain spasi atau tab. Di `ukur`, dua pembandingan mengenali pemisah; kenaikan penghitung mensyaratkan byte sekarang berisi teks dan byte sebelumnya berada di luar rentang. Deretan pemisah berturut-turut tidak menambah hitungan. Argumen kosong sah dengan hasil 0. Jika jumlah argumen salah, program mengirim pesan ke stderr dan mengembalikan 2.

Untuk cek silang, jalankan `objdump -d -M intel --disassemble=ukur program` dari direktori soal. Tandai cabang untuk spasi, tab, dan nilai sebelumnya. Urutan instruksi tergantung compiler. [Kasus pengujian](kasus.json) · [Sumber](program.c) · [Soal](../README.md)
