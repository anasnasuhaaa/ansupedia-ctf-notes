# GDB dan pwndbg sekali lihat

Mulai di shell dengan `pwndbg ./latihan` untuk distribusi mandiri, atau `gdb -q ./latihan` bila plugin dimuat dari konfigurasi GDB. Ketik semua perintah tabel di prompt debugger.

| Tujuan | GDB | Tambahan pwndbg |
| --- | --- | --- |
| Berhenti di batas fungsi | `break *jumlah`, `run` | `context regs` |
| Membaca lokasi eksekusi | `x/i $pc`, `disassemble main` | `context disasm` |
| Membaca stack | `x/3gx $rsp`, `bt` | `telescope $rsp 3` |
| Membaca rentang pemetaan pada Linux | `info proc mappings` | `vmmap` |
| Mengikuti satu instruksi atau kembali | `stepi`, `nexti`, `finish` | Baca ulang panel setelah berhenti |
| Menemukan bantuan lokal | `help x`, `apropos checkpoint` | `help telescope`, `help vmmap` |

Jika perintah tambahan tidak dikenali, periksa apakah sesi memakai pwndbg. Pastikan ada inferior yang berhenti sebelum membaca register. [Latihan GDB dan snapshot](../05-debugging.md)
