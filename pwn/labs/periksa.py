"""Jalankan dari direktori lab yang berisi program hasil kompilasi."""
import json
import subprocess
import sys
from pathlib import Path


def main():
    cases = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    for case in cases:
        data = bytes.fromhex(case.get("stdin_hex", ""))
        result = subprocess.run(
            ["./program", *case.get("argv", [])],
            input=data, capture_output=True, timeout=3,
        )
        actual = (result.returncode, result.stdout, result.stderr)
        expected = (case["status"], case["stdout"].encode(), case.get("stderr", "").encode())
        if actual != expected:
            raise SystemExit(f"{case['nama']}: diharapkan {expected!r}, diterima {actual!r}")
        print(f"lulus: {case['nama']}")


if __name__ == "__main__":
    main()
