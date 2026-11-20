# Mengikuti dua frame pemanggilan

**Tujuan.** Bedakan hasil fungsi dalam dan hasil yang dicetak. Siapkan Linux x86-64, C compiler, Make, Python 3, GDB dan [tabel ABI](../../../03-abi.md). Di shell dari direktori ini:

```sh
make
./program
make check
objdump -d -M intel --disassemble=tagihan program
gdb -q ./program
```

Cari instruksi yang menerima hasil `nilai`. Tulis prediksi berapa fungsi yang masih aktif saat `nilai` baru dimasuki. Kemudian, di **(gdb)**:

```gdb
break *nilai
run
info registers edi esi
bt
up
info args
down
finish
print/d $eax
finish
print/d $eax
```

Berhasil bila kamu dapat mengaitkan setiap hasil dengan fungsi yang baru kembali dan mencocokkan hasil terakhir dengan stdout. [Pembahasan](pembahasan.md) · [Indeks lab](../../README.md)
