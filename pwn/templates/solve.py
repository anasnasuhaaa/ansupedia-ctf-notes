#!/usr/bin/env python3
from pwn import *

exe = ELF("./demo", checksec=False)
context.binary = exe
context.timeout = 3


def conn():
    io = process([exe.path])
    if args.GDB:
        gdb.attach(io, gdbscript="""
set debuginfod enabled off
break lapor
commands
silent
print panjang
continue
end
continue
""")
    return io


def main():
    # Ubah contoh teks untuk menguji hipotesis tentang protokol lab sendiri.
    data = "kopi".encode("utf-8")
    with conn() as io:
        if io.recvuntil(b"teks> ") != b"teks> ":
            raise RuntimeError("Prompt demo belum diterima")
        io.sendline(data)
        reply = io.recvuntil(b"\n")
        if not reply.startswith(b"BYTE ") or not reply.endswith(b"\n"):
            raise ValueError(f"Balasan tidak lengkap: {reply!r}")
        field = reply[5:-1]
        if not field.isdigit() or int(field) != len(data):
            raise ValueError(f"Jumlah byte tidak sesuai: {reply!r}")
        print(f"Panjang terverifikasi: {int(field)} byte")


if __name__ == "__main__":
    main()
