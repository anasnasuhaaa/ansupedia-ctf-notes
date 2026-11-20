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
