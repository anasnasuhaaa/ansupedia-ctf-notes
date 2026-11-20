# Matriks checksec

Di shell jalankan `pwn checksec ./objek-kuat` pada [build contoh](../07-proteksi.md). Nama kolom tergantung alat dan versi.

| Laporan | Cocokkan | Pertanyaan yang dijawab |
| --- | --- | --- |
| NX enabled | `readelf -lW objek-kuat` → GNU_STACK tanpa E | Izin stack apa yang diminta ELF? |
| Canary found | `readelf -Ws objek-kuat` → stack_chk_fail; periksa disassembly fungsi | Fungsi mana yang benar-benar memeriksa penjaga? |
| PIE enabled | `file objek-kuat`, `readelf -hW objek-kuat` | Apakah citra executable mendukung relokasi? |
| Partial RELRO | GNU_RELRO pada header, tanpa permintaan NOW | Rentang mana menjadi hanya-baca setelah relokasi? |
| No RELRO | Periksa apakah program header GNU_RELRO absen | Apakah ELF meminta perlindungan rentang ini? |
| Full RELRO | GNU_RELRO serta NOW pada `readelf -dW objek-kuat` | Apakah resolusi segera diminta bersama proteksi rentang? |
| ASLR | `cat /proc/sys/kernel/randomize_va_space`, pengaturan GDB dan peta runtime | Apa kebijakan host dan bukti dari proses yang diamati? |

Jika `pwn` tidak tersedia, gunakan kolom tengah. Kesimpulan tentang bug tetap membutuhkan peninjauan operasi memori. [Contoh review](../06-keamanan-memori.md)
