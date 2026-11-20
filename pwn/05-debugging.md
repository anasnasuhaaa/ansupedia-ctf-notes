# Mengamati pemanggilan fungsi dengan GDB dan pwndbg

Gunakan [program latihan](README.md#siapkan-program-latihan) untuk memeriksa dua prediksi dari [konvensi pemanggilan](03-abi.md). Saat `jumlah` dimasuki, argumennya adalah 7 dan 5. Saat fungsi kembali ke `main`, hasilnya adalah 12.

## Berhenti di instruksi pertama

Jalankan `gdb -q ./latihan` dari terminal. Ketik perintah berikut di prompt GDB.

```gdb
set disassembly-flavor intel
break *jumlah
run
info registers edi esi
bt
```

Tanda `*` pada `break *jumlah` memilih alamat instruksi pertama fungsi. Di titik ini, `edi` berisi 7 dan `esi` berisi 5. GDB mungkin menampilkan nilai berbeda untuk parameter C pada baris pemberitahuan breakpoint karena instruksi penyalinan parameter ke stack belum berjalan. Baca register untuk memeriksa nilai yang baru diserahkan pemanggil.

Perintah `bt` (*backtrace*) menampilkan rantai pemanggilan. Bingkai `#0` adalah `jumlah`, yaitu fungsi yang sedang berjalan, dan `#1` adalah pemanggilnya, `main`.

## Ikuti satu instruksi dan baca hasil

```gdb
x/i $pc
si
x/i $pc
finish
print/d $eax
continue
quit
```

`x/i $pc` menampilkan instruksi pada alamat yang ditunjuk *program counter* (`rip` di x86-64). Perintah `si` menjalankan satu instruksi mesin. Bandingkan kedua keluaran `x/i` untuk melihat posisi eksekusi sebelum dan sesudah langkah itu.

`finish` menjalankan sisa fungsi hingga kembali ke `main`. Sekarang `print/d $eax` menampilkan 12 dalam desimal. Periksa register sebelum `continue` karena instruksi berikutnya dapat mengubahnya. Setelah dilanjutkan, program mencetak `hasil = 12` dan selesai.

## Mengulang pengamatan dengan pwndbg

Jika memakai pwndbg versi mandiri, jalankan `pwndbg ./latihan`. Jika pwndbg dimuat melalui konfigurasi GDB, gunakan `gdb -q ./latihan`. Ulangi `break *jumlah` dan `run`, lalu jalankan perintah berikut saat program berhenti.

```gdb
context regs
context disasm
```

Pada panel register, cocokkan `RDI` dan `RSI` dengan dua argumen tadi. Pada panel disassembly, cari penanda instruksi saat ini. Jalankan `si`, lalu tampilkan kembali `context disasm` untuk melihat penanda berpindah. Perintah `finish` dan `print/d $eax` juga berlaku pada sesi ini. [Dokumentasi context pwndbg](https://pwndbg.re/stable/commands/context/context/)

**Latihan mandiri.** Ubah hanya argumen pertama di sumber menjadi 9, lalu kompilasi ulang. Sebelum membuka debugger, tulis prediksimu untuk `edi` dan `esi` saat fungsi dimasuki serta `eax` saat kembali. Ulangi sesi di atas. Tiga titik pemeriksaan itu seharusnya menunjukkan 9, 5, dan 14.

[Indeks PWN](README.md) · [Indeks repositori](../README.md)

## Memilih titik pengamatan

Buka sesi baru dari shell dengan `gdb -q ./latihan`. Untuk bekerja luring, ketik `set debuginfod enabled off` di GDB sebelum memulai proses. Perintah berikut diketik di **(gdb)**:

```gdb
start
disassemble /s main
break *jumlah
continue
info frame
x/2gx $rsp
x/i $pc
```

`start` berhenti sementara di awal `main`. `run` memulai eksekusi dari awal; `continue` melanjutkan proses yang sedang berhenti. Saat baru memasuki `jumlah`, word pertama pada `rsp` berisi alamat kembali ke instruksi sesudah `call`. Cocokkan dengan listing `main`. Dalam `x/2gx`, angka 2 adalah jumlah unit, `g` berarti delapan byte dan `x` menampilkan heksadesimal. Gunakan `x/8bx $rsp` untuk melihat satu word sebagai delapan byte. Ini cara memeriksa little endian tanpa bergantung pada alamat contoh.

`stepi` mengeksekusi satu instruksi termasuk masuk ke fungsi pada `call`. `nexti` melewati pemanggilan itu sampai kembali, kecuali ada breakpoint atau sinyal. Di pwndbg, `telescope $rsp 3` menafsirkan tiga slot dan memperlihatkan rantai pointer bila dapat dibaca. `vmmap` memberi rentang dan izin pemetaan saat ini. Cari rentang yang memuat `$pc`, lalu yang memuat `$rsp`. Di GDB Linux biasa, gunakan `info proc mappings` dan periksa kolom yang tersedia pada versimu.

## Membaca snapshot

Saat berhenti di `jumlah`, ketik `generate-core-file jumlah.core` di GDB pada direktori latihan yang dapat ditulisi. Dari shell kedua, buka snapshot dengan `gdb -q ./latihan jumlah.core`. Di sesi snapshot:

```gdb
bt
frame 0
info registers rip rsp
x/i $pc
frame 1
info frame
```

Core menyimpan keadaan proses pada satu saat. Core buatan ini berasal dari breakpoint pada program sehat. Bandingkan rantai frame dan instruksi dengan sesi hidup. Untuk core akibat crash, simpan juga sinyal, build yang cocok dan input pengamatan. Frame teratas mengidentifikasi tempat proses berhenti; kerusakan data dapat terjadi lebih awal. Peringatan tentang halaman yang gagal disalin membatasi memori yang bisa diperiksa. Core dapat memuat data proses, jadi gunakan direktori latihan pribadi.

## Mengulang dari checkpoint

Buka sesi GDB hidup yang baru dengan biner yang sama. Pada Linux dengan dukungan fork untuk proses latihan, coba di **(gdb)**:

```gdb
start
checkpoint
info checkpoints
next
restart 1
x/i $pc
```

Gunakan ID hasil `info checkpoints` bila berbeda dari 1. Periksa apakah baris sumber dan instruksi kembali ke posisi sebelum `next`. Teks yang telanjur dicetak ke terminal atau perubahan di luar proses tetap dapat terlihat. Jika checkpoint tidak tersedia, ulangi `run` dengan breakpoint dan input yang sama. [Manual checkpoint GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Checkpoint_002fRestart.html)

**Uji diri.** Mengapa `continue` cocok di sesi hidup dan tidak dapat menggerakkan core? Jika sebuah perintah melaporkan “No registers”, periksa dulu apakah masih ada proses yang berhenti. Catatan yang bisa diulang menyebutkan build, input, titik berhenti dan ekspresi yang dibaca.

[Prasyarat ABI](03-abi.md) · [Pemeriksaan statis](04-pemeriksaan-biner.md)
