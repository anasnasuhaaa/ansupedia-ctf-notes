# Pembahasan Pagi

Kontrak masukan mensyaratkan persis dua byte lalu EOF. Byte pertama berbobot 1 dan byte kedua 256. Urutan `01 02` memberi 513, sedangkan `02 01` memberi 258. Data nol tetap dibaca karena program memakai jumlah hasil `fread`. Di shell, `echo` lazimnya menambah newline yang mengubah jumlah byte; gunakan `printf` pada soal. Satu byte tambahan, catatan terpotong atau kosong menghasilkan status 2.

Buka `objdump -d -M intel --disassemble=main program` di direktori soal. Ikuti dua pembacaan elemen setelah pengecekan EOF, lalu cari pergeseran delapan bit atau instruksi ekuivalen. Encoding dipilih eksplisit oleh kode sehingga pembuktiannya tidak bergantung pada endianness host. [Kasus pengujian](kasus.json) · [Sumber](program.c) · [Soal](../README.md)
