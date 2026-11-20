# Register System V AMD64

| Saat pengamatan | Lokasi | Contoh |
| --- | --- | --- |
| Masuk fungsi, integer/pointer sederhana | rdi, rsi, rdx, rcx, r8, r9; sisanya lewat stack | Dua int pertama di edi, esi |
| Sesudah kembali | eax untuk int, rax untuk pointer | Baca segera setelah finish |
| Sebelum call biasa | rsp kelipatan 16 untuk contoh integer sederhana | Saat baru masuk, (rsp + 8) kelipatan 16 |
| Selama langkah instruksi | rip menunjuk instruksi berikut, rsp ke puncak stack | `x/i $pc` dan `x/gx $rsp` di GDB |
| Nilai yang dipertahankan callee | rbx, rbp, r12–r15, serta pemulihan rsp | rbp bisa berfungsi sebagai frame pointer pada build debug |
| Lebar register | rax 64, eax 32, ax 16, al 8 bit | Penulisan eax mengosongkan 32 bit teratas rax |

Periksa register argumen pada instruksi pertama fungsi; sesudah panggilan berikut nilainya dapat berubah. Floating point, struktur dan system call memiliki aturan tersendiri. [Contoh call site](../03-abi.md) · [Lab frame](../labs/guided/frame/README.md)
