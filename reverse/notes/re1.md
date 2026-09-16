# Reverse Engineering CTF — RE #1 Cheatsheet Lanjutan

Cheatsheet ini digunakan untuk melakukan **triage awal binary** sebelum masuk ke Ghidra atau debugging.

Tujuan utamanya adalah menjawab:

* File ini sebenarnya apa?
* Arsitekturnya apa?
* Binary 32-bit atau 64-bit?
* Stripped atau tidak?
* Ada proteksi apa?
* Ada string atau fungsi menarik?
* Library apa yang digunakan?
* Seperti apa struktur awal programnya?

---

# 1. `ls -lah`

```bash
ls -lah chall
```

Contoh output:

```text
-rwxr-xr-x 1 anas anas 16K Sep 16 08:30 chall
```

Arti singkat:

```text
-rwxr-xr-x
```

adalah permission file.

```text
r = read
w = write
x = execute
```

Jika terdapat `x`, file dapat dieksekusi.

```text
16K
```

menunjukkan ukuran file.

### Hal yang diperhatikan

```text
Apakah executable?
Berapa ukuran binary?
Siapa pemilik file?
```

---

# 2. `file`

```bash
file chall
```

Contoh output:

```text
chall: ELF 64-bit LSB pie executable, x86-64,
dynamically linked,
interpreter /lib64/ld-linux-x86-64.so.2,
for GNU/Linux 3.2.0,
not stripped
```

## ELF

```text
ELF
```

Executable and Linkable Format.

Format executable yang umum digunakan pada Linux.

```text
Linux   → ELF
Windows → PE / EXE
macOS   → Mach-O
```

---

## 64-bit

```text
ELF 64-bit
```

Program menggunakan arsitektur 64-bit.

Register yang nantinya sering ditemui:

```text
RAX
RBX
RCX
RDX
RSP
RBP
RSI
RDI
```

Jika 32-bit biasanya menggunakan:

```text
EAX
EBX
ECX
EDX
ESP
EBP
```

---

## LSB

```text
LSB
```

Least Significant Byte.

Biasanya berarti binary menggunakan:

```text
Little Endian
```

Contoh nilai:

```text
0x12345678
```

di memory tersimpan:

```text
78 56 34 12
```

---

## x86-64

```text
x86-64
```

Menunjukkan arsitektur CPU binary.

Contoh arsitektur lain:

```text
x86
ARM
MIPS
RISC-V
```

Assembly setiap arsitektur berbeda.

Untuk CTF beginner biasanya banyak ditemui:

```text
x86-64
```

---

## PIE executable

```text
pie executable
```

PIE:

```text
Position Independent Executable
```

Artinya program dapat dimuat pada alamat memory yang berbeda ketika dijalankan.

Contoh:

```text
Run 1:
main = 0x555555551149

Run 2:
main = 0x565912341149
```

PIE biasanya bekerja bersama:

```text
ASLR
```

Untuk Reverse Engineering biasa, informasi ini cukup diketahui terlebih dahulu.

---

## Dynamically linked

```text
dynamically linked
```

Program menggunakan library eksternal saat berjalan.

Contohnya:

```c
printf()
scanf()
strcmp()
malloc()
```

biasanya berasal dari:

```text
libc
```

---

## Statically linked

Jika output menunjukkan:

```text
statically linked
```

berarti banyak library sudah ikut dimasukkan ke dalam binary.

Akibatnya ukuran binary biasanya lebih besar.

Contoh:

```text
Dynamic binary:
20 KB

Static binary:
700 KB+
```

Static binary juga dapat menghasilkan jumlah fungsi yang jauh lebih banyak ketika dibuka di Ghidra.

---

## Not stripped

```text
not stripped
```

Artinya symbol masih tersedia.

Nama fungsi seperti:

```text
main
win
check_password
verify
decrypt
```

mungkin masih dapat ditemukan.

Ini sangat membantu Reverse Engineering.

---

## Stripped

```text
stripped
```

Artinya sebagian besar nama symbol telah dihapus.

Misalnya sebelumnya:

```text
check_password
```

di Ghidra mungkin hanya terlihat sebagai:

```text
FUN_00101230
```

Reverse engineer perlu menentukan sendiri fungsi tersebut melakukan apa.

---

# 3. `strings`

```bash
strings chall
```

Command ini mencari data printable seperti:

```text
ASCII string
pesan program
password
URL
nama file
flag
error message
```

Contoh output:

```text
Enter password:
Wrong password!
Correct!
flag.txt
strcmp
s3cr3t
```

### Interpretation

Jika terdapat:

```text
Enter password:
Wrong password!
Correct!
```

kemungkinan program memiliki mekanisme pengecekan input.

Jika ditemukan:

```text
flag.txt
```

kemungkinan program membaca flag dari file.

Jika ditemukan:

```text
strcmp
```

kemungkinan ada perbandingan string.

---

## Membuka dengan `less`

```bash
strings chall | less
```

Useful command:

```text
/search
```

Contoh:

```text
/password
```

Untuk keluar:

```text
q
```

---

## Filter menggunakan `grep`

```bash
strings chall | grep -i password
```

atau:

```bash
strings chall | grep -Ei "flag|password|secret|correct|wrong"
```

`-i`:

```text
case insensitive
```

`-E`:

```text
extended regular expression
```

---

# 4. `checksec`

```bash
checksec --file=chall
```

Contoh output:

```text
RELRO           STACK CANARY      NX            PIE
Partial RELRO   No canary found   NX enabled    PIE enabled
```

`checksec` digunakan untuk melihat proteksi keamanan binary.

Lebih penting di Pwn, tetapi tetap berguna dalam RE.

---

## RELRO

Contoh:

```text
Partial RELRO
```

atau:

```text
Full RELRO
```

RELRO:

```text
Relocation Read-Only
```

Berfungsi melindungi struktur tertentu seperti:

```text
GOT
```

dari modifikasi.

Level:

```text
No RELRO
Partial RELRO
Full RELRO
```

Secara sederhana:

```text
Full RELRO > Partial RELRO > No RELRO
```

dalam hal proteksi.

Untuk RE biasa belum terlalu penting.

---

# 5. Stack Canary

Contoh:

```text
Canary found
```

atau:

```text
No canary found
```

Stack Canary digunakan untuk mendeteksi:

```text
stack buffer overflow
```

Konsep sederhananya:

```text
buffer
canary
saved stack data
```

Jika buffer overflow mengubah canary, program mendeteksinya dan biasanya berhenti.

Lebih penting untuk Pwn daripada RE.

---

# 6. NX

Contoh:

```text
NX enabled
```

NX:

```text
No Execute
```

Artinya area memory seperti stack tidak boleh langsung digunakan untuk menjalankan kode.

Jika:

```text
NX enabled
```

biasanya shellcode tidak dapat langsung dijalankan dari stack.

Lagi-lagi lebih relevan untuk Pwn.

---

# 7. PIE

Contoh:

```text
PIE enabled
```

Artinya alamat binary dapat berubah setiap program dijalankan.

Contoh:

```text
run 1:
0x555555554000

run 2:
0x563211234000
```

Jika:

```text
No PIE
```

alamat program cenderung tetap.

---

# Ringkasan `checksec`

Misalnya:

```text
RELRO           Canary        NX          PIE
Full RELRO      Canary found  NX enabled  PIE enabled
```

Interpretasi sederhana:

```text
RELRO → proteksi GOT
Canary → proteksi stack overflow
NX → memory stack tidak executable
PIE → alamat binary berubah
```

Untuk RE:

```text
Tidak perlu terlalu fokus dahulu.
```

Untuk Pwn:

```text
Sangat penting.
```

---

# 8. `ldd`

```bash
ldd chall
```

Contoh output:

```text
linux-vdso.so.1
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
/lib64/ld-linux-x86-64.so.2
```

Digunakan untuk melihat:

```text
shared library dependency
```

---

## `libc.so.6`

Library standar C Linux.

Berisi fungsi seperti:

```text
printf
puts
scanf
strcmp
strlen
malloc
free
read
write
```

Jika binary dynamically linked, hampir pasti kamu akan sering melihat libc.

---

## `ld-linux`

Contoh:

```text
/lib64/ld-linux-x86-64.so.2
```

Merupakan:

```text
dynamic linker / loader
```

Tugasnya membantu memuat library ketika program dijalankan.

---

# 9. `readelf -h`

```bash
readelf -h chall
```

Menampilkan:

```text
ELF Header
```

Contoh:

```text
Class:                             ELF64
Data:                              2's complement, little endian
Type:                              DYN
Machine:                           Advanced Micro Devices X86-64
Entry point address:               0x1080
```

---

## Class

```text
ELF64
```

Berarti:

```text
64-bit
```

Jika:

```text
ELF32
```

berarti:

```text
32-bit
```

---

## Data

```text
little endian
```

Menunjukkan byte order binary.

---

## Type

Contoh:

```text
DYN
```

Sering muncul pada:

```text
PIE executable
shared object
```

Kemungkinan lain:

```text
EXEC
```

biasanya executable non-PIE.

---

## Machine

```text
Advanced Micro Devices X86-64
```

Menunjukkan CPU architecture:

```text
x86-64
```

---

## Entry Point

```text
Entry point address: 0x1080
```

Merupakan alamat pertama tempat program mulai dieksekusi.

Penting:

```text
Entry Point != selalu main()
```

Biasanya:

```text
Entry Point
   ↓
_start
   ↓
runtime initialization
   ↓
main()
```

---

# 10. `readelf -s`

```bash
readelf -s chall
```

Digunakan untuk melihat:

```text
symbol table
```

Contoh:

```text
34: 0000000000001169 37 FUNC GLOBAL DEFAULT 15 win
35: 000000000000118e 76 FUNC GLOBAL DEFAULT 15 check_password
36: 00000000000011da 98 FUNC GLOBAL DEFAULT 15 main
```

Bagian penting:

```text
FUNC
```

berarti symbol merupakan fungsi.

Contoh symbol:

```text
win
check_password
main
```

---

## Filter symbol

```bash
readelf -s chall | grep main
```

atau:

```bash
readelf -s chall | grep -E "win|flag|check|verify"
```

---

# 11. `nm`

```bash
nm chall
```

`nm` digunakan untuk melihat symbol binary dengan output yang lebih sederhana.

Contoh:

```text
0000000000001169 T win
000000000000118e T check_password
00000000000011da T main
```

---

## Huruf `T`

```text
T
```

menunjukkan symbol berada pada bagian:

```text
.text
```

Biasanya berarti:

```text
function / executable code
```

Maka:

```bash
nm chall | grep " T "
```

bisa digunakan untuk melihat fungsi.

---

## Jika binary stripped

```bash
nm chall
```

bisa menghasilkan:

```text
nm: chall: no symbols
```

Ini tanda binary kemungkinan:

```text
stripped
```

---

# 12. `objdump`

```bash
objdump -d chall
```

Digunakan untuk:

```text
disassembly
```

Artinya mengubah machine code menjadi assembly.

---

## Intel Syntax

Gunakan:

```bash
objdump -d -M intel chall
```

Contoh:

```asm
00000000000011da <main>:
    push   rbp
    mov    rbp,rsp
    sub    rsp,0x40
    call   118e <check_password>
    test   eax,eax
    je     1210
    call   1169 <win>
```

---

## `<main>`

```text
<main>
```

menandakan nama fungsi.

---

## `call`

```asm
call check_password
```

Artinya program memanggil fungsi:

```c
check_password();
```

---

## `test`

Contoh:

```asm
test eax,eax
```

Sering digunakan untuk mengecek apakah:

```text
EAX == 0
```

Return value fungsi biasanya berada di:

```text
RAX / EAX
```

---

## `je`

```asm
je address
```

Artinya:

```text
Jump if Equal
```

atau kondisi sebelumnya bernilai sama / zero.

Nanti akan dibahas lebih dalam di RE #2.

---

# 13. Mencari fungsi dengan `objdump`

Cari `main`:

```bash
objdump -d -M intel chall | grep -A30 "<main>"
```

`-A30` berarti:

```text
tampilkan 30 baris setelah hasil ditemukan
```

---

## Contoh

```asm
call   check_password
test   eax,eax
je     wrong
call   win
```

Walaupun belum memahami assembly mendalam, kita sudah bisa membuat gambaran:

```text
check_password()
       ↓
cek return value
       ↓
 benar? ───→ win()
       ↓
 salah
```

---

# 14. `objdump -t`

```bash
objdump -t chall
```

Digunakan untuk melihat:

```text
symbol table
```

Mirip dengan:

```bash
nm chall
```

dan:

```bash
readelf -s chall
```

Biasanya saya lebih memilih:

```text
nm
```

untuk pemeriksaan cepat.

---

# 15. Menjalankan Binary

```bash
./chall
```

Jangan langsung mencoba exploit.

Amati dulu:

```text
Apa yang diminta?
Apa yang dicetak?
Ada error?
Input apa yang diterima?
Ada perbedaan output?
```

Contoh:

```text
Enter password:
```

Coba:

```text
AAAA
```

Output:

```text
Wrong password!
```

Kita mendapatkan informasi:

```text
Program melakukan validasi terhadap input.
```

---

# 16. Permission Denied

Jika:

```bash
./chall
```

menghasilkan:

```text
Permission denied
```

cek:

```bash
ls -l chall
```

Jika belum executable:

```bash
chmod +x chall
```

Kemudian:

```bash
./chall
```

---

# 17. Command Triage Standar

Workflow sederhana:

```bash
file chall

ls -lah chall

./chall

strings chall | less

checksec --file=chall

ldd chall

readelf -h chall

nm chall

objdump -d -M intel chall | less
```

---

# 18. Workflow Lebih Cepat untuk CTF

Biasanya saya akan melakukan:

```bash
file chall
```

kemudian:

```bash
checksec --file=chall
```

kemudian:

```bash
strings chall | less
```

kemudian:

```bash
nm chall | grep " T "
```

jika binary `not stripped`.

Setelah itu:

```bash
./chall
```

Kemudian baru:

```text
Ghidra
```

atau:

```text
GDB
```

---

# 19. Pertanyaan yang Harus Dijawab Saat Triage

Setelah menjalankan command-command tadi, usahakan kamu bisa menjawab:

```text
1. Ini file apa?

2. Binary Linux atau Windows?

3. Arsitekturnya apa?

4. 32-bit atau 64-bit?

5. Little endian atau big endian?

6. PIE atau tidak?

7. Dynamic atau static?

8. Stripped atau tidak?

9. Ada string menarik apa?

10. Ada fungsi menarik apa?

11. Library apa yang digunakan?

12. Apa input yang diminta program?

13. Apa output ketika input salah?

14. Fungsi mana yang kemungkinan melakukan validasi?

15. Fungsi mana yang kemungkinan menghasilkan flag?
```

---

# 20. Cheat Sheet Super Singkat

```bash
# Identifikasi binary
file chall

# Permission + size
ls -lah chall

# Jalankan program
./chall

# Printable strings
strings chall
strings chall | less

# Cari clue
strings chall | grep -Ei "flag|password|secret|correct|wrong"

# Proteksi binary
checksec --file=chall

# Library dependency
ldd chall

# ELF header
readelf -h chall

# Symbol table
readelf -s chall

# Symbol sederhana
nm chall

# Function symbols
nm chall | grep " T "

# Disassembly
objdump -d -M intel chall

# Main function
objdump -d -M intel chall | grep -A30 "<main>"
```

---

# Mental Mapping

Biasakan mengingat:

```text
file
↓
"Ini file apa?"
```

```text
strings
↓
"Ada clue apa?"
```

```text
checksec
↓
"Binary punya proteksi apa?"
```

```text
ldd
↓
"Library apa yang digunakan?"
```

```text
readelf
↓
"Struktur ELF-nya bagaimana?"
```

```text
nm
↓
"Nama fungsi apa yang masih terlihat?"
```

```text
objdump
↓
"CPU sebenarnya menjalankan instruksi apa?"
```

```text
Ghidra
↓
"Bisakah logika assembly diterjemahkan menjadi bentuk C-like?"
```

```text
GDB
↓
"Apa yang sebenarnya terjadi ketika program sedang berjalan?"
```

---

# Prinsip Penting RE #1

Jangan langsung mencoba memahami seluruh binary.

Gunakan pola:

```text
Recon
↓
Cari clue
↓
Cari fungsi menarik
↓
Cari alur validasi
↓
Fokus hanya pada bagian penting
```

Tujuan seorang Reverse Engineer bukan:

```text
"Membaca seluruh program."
```

Tetapi:

```text
"Menemukan bagian program yang menentukan jawaban challenge."
```

---

# Status Belajar

Jika sudah memahami isi dokumen ini, minimal kamu sudah dapat melakukan:

```text
Binary reconnaissance / triage
```

dan siap masuk ke:

```text
RE #2 — Dasar Assembly x86-64 untuk Reverse Engineering CTF
```

Materi berikutnya akan mulai membahas:

```text
register
mov
lea
cmp
test
jmp
je
jne
call
ret
stack
RSP
RBP
RAX
RDI
RSI
```

Tujuannya bukan menjadi programmer Assembly, tetapi mampu membaca potongan seperti:

```asm
mov eax,DWORD PTR [rbp-0x4]
cmp eax,0x5
jne wrong
```

dan memahami bahwa secara kasar itu berarti:

```c
if (value != 5) {
    // wrong
}
```
