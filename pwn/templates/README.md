# Interaksi dengan proses lokal

**Tujuan.** Bangun klien yang menunggu prompt, mengirim satu baris dan menguji isi balasan. Siapkan Linux x86-64, C compiler, Make, Python 3 dan pwntools. Baca [representasi data dan ABI](../03-abi.md) terlebih dahulu. Struktur `conn()` dan `main()` mengikuti kebiasaan pwninit; seluruh latihan memakai program penghitung byte di folder ini.

Di shell dari akar repo:

```sh
cd pwn/templates
make demo
printf 'kopi\n' | ./demo
python3 solve.py
python3 solve.py DEBUG
```

Protokol terdiri dari prompt `teks> ` (dengan spasi, tanpa newline), satu baris masukan, lalu balasan `BYTE n\n`. Nol sampai 32 byte sebelum newline diterima, termasuk spasi. EOF sebelum newline atau byte ke-33 menghasilkan pesan di stderr dan status gagal. `fflush` membuat prompt tersedia sebelum proses mulai membaca. Klien memeriksa awalan, terminator dan angka. Smoke test lulus bila klien keluar normal dan mencetak `Panjang terverifikasi: 4 byte`.

`ELF("./demo")` membaca metadata berkas di direktori kerja. `context.binary = exe` menyetel arsitektur, lebar word dan endianness sesuai ELF itu. `conn()` memulai proses lokal; `main()` menangani protokol. Jalankan `python3 solve.py GDB` dari sesi dengan terminal yang didukung pwntools (misalnya di dalam tmux) dan izin ptrace. Debugger memasang breakpoint di `lapor`, mencetak argumen panjang, lalu melanjutkan otomatis. Sakelar `DEBUG` menampilkan lalu lintas byte di terminal klien. [Template Python](solve.py) · [Sumber demo C](demo.c)

### Membaca dan mengirim byte

| Operasi pada tube | Arti pada demo |
| --- | --- |
| `io.recvuntil(b"teks> ")` | Tunggu pembatas lengkap. Timeout menghasilkan byte kosong; EOF sebelum pembatas dapat menimbulkan EOFError. Periksa hasil sebelum mengirim. |
| `io.send(b"kopi")` | Kirim empat byte; demo masih menunggu akhir baris. Kirim `io.send(b"\n")` untuk menyelesaikan. |
| `io.sendline(b"kopi")` | Kirim isi dan newline sesuai konfigurasi tube. |
| `io.sendafter(b"teks> ", b"kopi\n")` | Gabungkan recvuntil dan send. Pada timeout tahap penerimaan, helper masih dapat mengirim; gunakan dua operasi eksplisit bila prompt wajib divalidasi. |
| `io.recvuntil(b"\n")` | Baca satu balasan lengkap; simpan dalam bytes sampai batas protokol dan field terverifikasi. |

Di Python, `str` berisi karakter Unicode. Contoh `"é".encode("utf-8")` panjangnya dua byte. Gunakan `.decode("utf-8")` pada **field teks** sesuai encoding yang disepakati. `int(b"12")` membaca digit desimal. Untuk bilangan **biner** dengan lebar tetap, uji di shell:

```sh
python3 - <<'PY'
from pwn import context, p8, p16, p32, p64, u32, u64
context.clear(arch="amd64", endian="little")
assert p8(7) == b"\x07"
assert p16(0x1234) == bytes.fromhex("34 12")
assert p32(12) == bytes.fromhex("0c 00 00 00")
assert u32(p32(12)) == u64(p64(12)) == 12
PY
```

Angka pada balasan demo berbentuk ASCII; `u32` memerlukan empat byte biner. Jika klien berhenti menunggu, periksa spasi akhir prompt, newline pada masukan, serta apakah proses sudah keluar. Simpan timeout agar salah ketik tidak membuat tes menggantung.

**Uji diri.** Prediksi balasan untuk satu spasi, baris kosong, dan “é”. Ubah `data` dalam salinan template, jalankan dua kali, lalu cocokkan hasil dengan jumlah byte encoding. Urutan yang bisa diuji ulang adalah tunggu prompt → kirim baris → validasi field.

[Debugging](../05-debugging.md) · [Indeks PWN](../README.md) · [Referensi tube pwntools](https://docs.pwntools.com/en/stable/tubes.html)
