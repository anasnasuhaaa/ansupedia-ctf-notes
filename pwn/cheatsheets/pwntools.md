# Pwntools untuk penghitung byte

Mulai dari shell di `pwn/templates` dengan `make demo` dan `python3 solve.py DEBUG`. Cuplikan tabel adalah Python.

| Maksud | Ekspresi | Periksa |
| --- | --- | --- |
| Baca arsitektur dari ELF lokal | `context.binary = ELF("./demo", checksec=False)` | `context.arch`, `context.bits`, `context.endian` |
| Mulai proses | `io = process(["./demo"])` | Satu proses melayani satu baris |
| Sinkronisasi | `io.recvuntil(b"teks> ", timeout=2)` | Bandingkan dengan prompt lengkap |
| Input | `io.sendline("é".encode("utf-8"))` | Dua byte isi, satu newline |
| Balasan | `io.recvuntil(b"\n", timeout=2)` | Harapkan `b"BYTE 2\n"`; bedakan timeout dan EOF |
| Bilangan biner | `u32(p32(12))`, `u64(p64(12))` | Ukuran dan endian disepakati dahulu |
| Bilangan teks | `int(b"12")` | Validasi field digit sebelum konversi |

[Template dengan conn dan main](../templates/README.md) · [Lab protokol](../labs/guided/protokol/README.md)
