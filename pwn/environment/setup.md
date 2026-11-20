# Menyiapkan mesin latihan

Gunakan Linux x86-64 dan toolchain native agar ABI sesuai dengan contoh. Pada Ubuntu yang memiliki akses paket, pasang alat dasar sebelum sesi luring. Dari shell:

```sh
sudo apt install build-essential binutils file gdb python3 python3-venv
uname -m
gcc --version
ld --version
make --version
gdb --version
python3 --version
```

Untuk pwntools, gunakan Python yang sudah dapat mengimpor paket atau siapkan venv di luar repo. Jika memasang dari internet pada masa persiapan, jalankan di shell:

```sh
python3 -m venv ~/venv-catatan-pwn
. ~/venv-catatan-pwn/bin/activate
python -m pip install pwntools
python -c 'from importlib.metadata import version; print(version("pwntools"))'
```

Untuk pemasangan luring, buat arsip wheel **beserta dependensinya** saat masih terhubung, misalnya `python -m pip wheel --wheel-dir ~/wheel-pwn pwntools` pada mesin dengan OS, arsitektur dan versi Python yang cocok. Di venv baru yang cocok, uji `python -m pip install --no-index --find-links ~/wheel-pwn pwntools`. Beberapa paket memerlukan compiler atau header sistem saat membangun wheel. Simpan versi yang sudah diuji dan cadangkan arsipnya.

Pwndbg opsional menambah panel debugger. Gunakan paket yang cocok dengan GDB/Python atau distribusi mandiri, lalu periksa `help vmmap` di sesi yang dibuka. Ghidra atau IDA diperlukan hanya untuk jalur GUI. Workflow Python di handbook memakai struktur yang lazim di pwninit; template sudah disediakan dan berjalan langsung. [Panduan pwndbg](https://pwndbg.re/stable/setup/) · [Template lokal](../templates/README.md)

Sebagai tes mesin, mulai dari akar repo dan jalankan `make -C pwn/labs/guided/frame check`, lalu `make -C pwn/labs/guided/protokol check`. Tes pertama memeriksa compiler dan Python; tes kedua juga memerlukan pwntools. [Checklist luring](offline-checklist.md)
