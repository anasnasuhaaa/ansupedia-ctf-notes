# Menemukan rujukan tanpa internet

| Pertanyaan | Di terminal lokal | Rujukan daring opsional saat persiapan |
| --- | --- | --- |
| Bagaimana membaca ELF? | `man 5 elf`, `readelf --help`, `info binutils` | [Manual GNU Binutils](https://sourceware.org/binutils/docs/binutils/) |
| Kapan register berubah? | Di GDB: `help info registers`, `help finish` | [System V AMD64 psABI](https://gitlab.com/x86-psABIs/x86-64-ABI) |
| Bagaimana memeriksa core? | `man gdb`, di GDB: `help core-file` | [Manual GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/) |
| Apa yang dikembalikan recvuntil? | `python3 -m pydoc pwnlib.tubes.tube.tube.recvuntil` | [Dokumentasi pwntools](https://docs.pwntools.com/en/stable/tubes.html) |
| Bagaimana membaca peta memori? | Di pwndbg: `help vmmap` | [Dokumentasi vmmap](https://pwndbg.re/stable/commands/memory/vmmap/) |

Paket manual dan Info dapat terpisah pada distribusi minimal. Coba tiap perintah sebelum berangkat; bila manual tidak terpasang, gunakan bantuan bawaan alat dan [cheatsheet perintah](../cheatsheets/commands.md).
