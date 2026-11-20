# Pengantar allocator, kebocoran informasi, dan batas proses

**Tujuan.** Kenali istilah yang bergantung pada versi runtime dan sebutkan batas bukti saat membaca diagnostik. Prasyaratnya adalah [kepemilikan memori](00-memori-c.md) dan [proteksi ELF](07-proteksi.md).

Saat `free` selesai, kontrak C mengakhiri masa hidup alokasi. Allocator dapat menyimpan ruang itu untuk permintaan berikutnya. Pada glibc, *arena* mengelola sumber daya alokasi dan *tcache* adalah cache per-thread untuk kelompok ukuran tertentu. Versi, konfigurasi, ukuran dan riwayat alokasi memengaruhi penggunaan cache. Dua pemanggilan `malloc` boleh menghasilkan alamat yang sama pada waktu berbeda; kesamaan alamat tidak memulihkan hak memakai pointer lama. [Manual allocator glibc](https://sourceware.org/glibc/manual/latest/html_node/Memory-Allocation-Tunables.html)

**Kebocoran informasi** terjadi saat data melewati batas yang dimaksud aplikasi, misalnya log mencetak alamat atau byte sisa di bagian buffer yang belum terisi. Ini berbeda dari *memory leak*, yaitu alokasi yang tidak dilepas ketika sudah selesai dipakai. Untuk meninjau fungsi yang mencatat hasil pembacaan, ikuti banyaknya byte yang benar-benar diisi dan siapa yang dapat membaca log. Simpan jumlah byte atau kode status bila cukup untuk diagnosis.

**Seccomp** membatasi system call yang boleh dilakukan thread Linux. Sebuah filter dapat mengembalikan error, mengirim sinyal atau melakukan tindakan lain sesuai kebijakan. Proses yang gagal membuka berkas juga dapat terbentur izin filesystem; pesan gagal saja belum menentukan penyebabnya. [Dokumentasi kernel](https://docs.kernel.org/userspace-api/seccomp_filter.html)

Di shell Linux pada mesin berbasis glibc:

```sh
getconf GNU_LIBC_VERSION
grep -E '^(Seccomp|NoNewPrivs):' /proc/$$/status
lscpu
readelf -nW objek-kuat
```

Perintah kedua membaca status **shell** saat ini. Seccomp 0 berarti nonaktif, 1 mode ketat dan 2 mode filter; angka itu tidak merinci isi kebijakan. Untuk proses lain yang kamu jalankan sendiri, periksa PID proses tersebut. Di x86-64, ekstensi seperti CET mencakup IBT untuk tujuan cabang tidak langsung dan shadow stack untuk pemeriksaan alamat kembali. Catatan properti GNU dapat menyatakan fitur pada berkas. Dukungan CPU, kernel, loader, serta status pengaktifan pada proses ikut menentukan efek runtime. [Dokumentasi shadow stack x86](https://docs.kernel.org/arch/x86/shstk.html)

**Uji diri.** Jika `free` tidak segera menurunkan penggunaan memori proses, informasi apa yang masih diperlukan sebelum menyimpulkan terjadi memory leak? Mengapa status seccomp terminal belum menjawab kebijakan sebuah program anak sesudah inisialisasi?

[Latihan debugging](05-debugging.md) · [Indeks PWN](README.md)
