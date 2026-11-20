# Catatan CTF Ansupedia

Kumpulan catatan belajar Capture the Flag (CTF) dalam bahasa Indonesia. Untuk mulai membaca program Linux x86-64, ikuti jalur PWN. Untuk mencari pembahasan per alat atau topik, gunakan indeks di bawah.

## PWN

[Dasar PWN di Linux x86-64](pwn/README.md) memakai satu program C untuk mempelajari format ELF, membaca assembly, mengikuti pemanggilan fungsi, memeriksa berkas biner, dan mengamati program di debugger.

## Reverse engineering

1. Kenali format berkas, simbol, dan alat inspeksi melalui [catatan pemeriksaan awal](reverse/notes/re1.md).
2. Cari penjelasan instruksi, register, dan percabangan di [catatan assembly x86-64](reverse/notes/re2-assembly.md).
3. Pelajari navigasi fungsi dan referensi silang di [catatan IDA](reverse/notes/RE-03-IDA.md).

## Web exploitation

Contoh disimpan per topik di direktori `web-exploitation/`.

- [2FA, Base64, dan zlib](web-exploitation/2fa/base64zlib.py)
- [SQL injection dasar](web-exploitation/sql-injection/basic.sql)
- [Server-side template injection (SSTI)](web-exploitation/ssti/payload.md)
