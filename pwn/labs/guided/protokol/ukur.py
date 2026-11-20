from pwn import context, process

context.log_level = "error"


def ukur(data):
    with process(["./demo"]) as io:
        if io.recvuntil(b"teks> ", timeout=2) != b"teks> ":
            raise RuntimeError("Prompt tidak lengkap")
        io.sendline(data)
        reply = io.recvuntil(b"\n", timeout=2)
        expected = b"BYTE %d\n" % len(data)
        if reply != expected:
            raise ValueError(f"{data!r}: {reply!r}, diharapkan {expected!r}")
        return reply


if __name__ == "__main__":
    for data in (b"", b" ", "é".encode("utf-8"), b"x" * 32):
        print(f"{data!r} -> {ukur(data)!r}")
