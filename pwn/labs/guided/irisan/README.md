# Membaca irisan array

**Tujuan.** Buktikan hubungan pointer awal, panjang tersisa, dan penjumlahan. Siapkan Make, compiler C, Python 3 dan GDB; baca [objek C](../../../00-memori-c.md). Mulai dari direktori ini di shell:

```sh
make
./program
make check
gdb -q ./program
```

Setiap baris berisi banyak elemen tersisa dan jumlah nilainya. Pilih baris ketiga, prediksi elemen pertama pada panggilan itu dan jelaskan mengapa alamat sesudah elemen terakhir boleh dibentuk pada iterasi terakhir. Di **(gdb)**:

```gdb
break jumlah if banyak == 2
run
print banyak
x/2ub awal
bt
finish
```

Cocokkan dua byte dan nilai kembali dengan baris pilihan. Berhasil bila tes keluaran lulus dan kamu dapat menjelaskan kondisi loop untuk irisan kosong. [Pembahasan](pembahasan.md) · [Indeks lab](../../README.md)
