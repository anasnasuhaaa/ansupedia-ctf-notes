# Perintah menurut pertanyaan

| Konteks | Perintah | Baca |
| --- | --- | --- |
| Shell | `file latihan`, `readelf -hW latihan` | Kelas, arsitektur, tipe berkas |
| Shell | `readelf -SW latihan`, `readelf -lW latihan` | Nama section, pemetaan ke segmen, izin |
| Shell | `readelf -dW latihan`, `readelf -rW latihan` | Dependensi langsung dan relokasi |
| Shell | `nm -n latihan`, `nm -D latihan` | Simbol biasa dan dinamis |
| Shell | `objdump -d -M intel --disassemble=jumlah latihan` | Urutan instruksi satu fungsi |
| Shell | `strings -a -t x latihan` | String beserta offset berkas |
| Shell | `gdb -q ./latihan` | Buka debugger dengan simbol program |
| (gdb) | `start`, `bt`, `info frame` | Berhenti di main dan identifikasi frame |
| (gdb) | `x/i $pc`, `x/8bx $rsp` | Instruksi berikut dan delapan byte stack |
| Shell | `python3 -m pydoc pwnlib.tubes.tube` | Bantuan API Python yang terpasang |

[Pemeriksaan awal](../04-pemeriksaan-biner.md) · [Referensi debugger](pwndbg.md)
