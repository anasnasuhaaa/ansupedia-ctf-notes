# Membaca proteksi ELF dan proses

**Tujuan.** Tentukan bukti yang diperlukan untuk menjelaskan proteksi sebuah build. Siapkan sumber dari [bab memori](00-memori-c.md) dan pahami [program header ELF](01-elf.md). Di shell:

```sh
gcc -std=c17 -g -O0 -Wall -Wextra -fstack-protector-strong -fPIE -pie -Wl,-z,relro,-z,now,-z,noexecstack -o objek-kuat objek.c
./objek-kuat
pwn checksec ./objek-kuat
readelf -lW objek-kuat
readelf -dW objek-kuat
readelf -Ws objek-kuat
cat /proc/sys/kernel/randomize_va_space
```

| Indikator umum | Apa yang dilakukan | Bukti dan batas kesimpulan |
| --- | --- | --- |
| NX enabled | Izin halaman mengendalikan eksekusi instruksi | Cari `GNU_STACK` tanpa flag E untuk permintaan stack non-eksekutabel; periksa izin aktual menggunakan peta proses |
| Canary found | Compiler menyisipkan nilai penjaga pada frame terpilih dan memeriksanya sebelum keluar | Cari rujukan ke `__stack_chk_fail` dan bandingkan prolog/epilog dua fungsi; hasil alat berlaku pada tingkat berkas |
| PIE enabled | Executable dapat direlokasi sebagai satu citra | Periksa tipe DYN dengan identifikasi executable PIE. Offset dalam build tetap berguna relatif ke citra |
| ASLR (kebijakan OS) | Kernel dapat mengacak lokasi pemuatan stack, pustaka, dan citra PIE | Nilai sysctl Linux 0/1/2 menunjukkan mode sistem; debugger dan konfigurasi proses dapat memengaruhi tiap run |
| Partial RELRO | Loader membuat rentang GNU_RELRO hanya-baca setelah relokasi awal | Cari `GNU_RELRO`; pada konfigurasi lazy binding masih ada slot panggilan yang perlu diperbarui |
| Full RELRO | Linker menata data relokasi untuk perlindungan dan meminta resolusi segera | Cocokkan `GNU_RELRO` dengan `BIND_NOW` atau flag `NOW`. Halaman data aplikasi lainnya masih dapat ditulis |

Build di atas meminta PIE, stack non-eksekutabel, proteksi stack kuat, dan full RELRO. Bandingkan dengan build standar `objek`: distribusi bisa mengaktifkan sebagian opsi secara bawaan. Di shell, buka `gdb -q ./objek-kuat`. Di **(gdb)** jalankan `start`, `show disable-randomization`, dan `info proc mappings`. Cocokkan izin halaman citra dengan program header. Alamat stack yang berulang dalam debugger perlu dibaca bersama pengaturan randomisasinya.

**Uji diri.** Jika sebuah ELF bertipe DYN, data tambahan apa yang mengidentifikasinya sebagai executable PIE? Mengapa “Canary found” belum cukup untuk menjelaskan proteksi fungsi `salin`? Ringkas bukti dengan mencatat apakah sumbernya compiler, metadata ELF, atau keadaan proses hidup.

[Kontrak memori C](06-keamanan-memori.md) · [Konsep lanjut](08-konsep-lanjut.md) · [Opsi linker GNU](https://sourceware.org/binutils/docs/ld/Options.html)
