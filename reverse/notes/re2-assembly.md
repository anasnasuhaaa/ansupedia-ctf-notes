# Reverse Engineering CTF — RE #2
## Dasar Assembly x86-64 untuk Reverse Engineering

Dokumen ini adalah catatan ringkas untuk memahami assembly x86-64 dalam konteks CTF Reverse Engineering.

Tujuan utama bukan menghafal seluruh instruksi assembly, tetapi mampu:

- memahami aliran data,
- mengenali fungsi,
- membaca kondisi,
- mengikuti percabangan,
- mengenali loop,
- menerjemahkan assembly ke bentuk C-like,
- menemukan syarat menuju jalur `correct`, `win`, atau flag.

---

# 1. Gambaran Umum

Program C:

```c
int angka = 5;

if (angka == 5) {
    printf("Benar\n");
}
```

setelah dikompilasi berubah menjadi:

```text
C Source
   ↓
Compiler
   ↓
Assembly
   ↓
Machine Code
```

Contoh machine code:

```text
b8 05 00 00 00
```

Dapat direpresentasikan sebagai assembly:

```asm
mov eax, 5
```

Tools seperti berikut membantu melihat assembly:

```text
objdump
Ghidra
GDB
```

---

# 2. Instruksi Penting yang Harus Dikenali

Untuk RE beginner, prioritaskan:

```text
mov
lea

add
sub
imul
xor

cmp
test

jmp
je / jz
jne / jnz
jg
jl
jge
jle

call
ret

push
pop
```

Tidak perlu menghafal seluruh instruction set x86-64.

---

# 3. Register x86-64

Register adalah tempat penyimpanan kecil dan cepat milik CPU.

Contoh:

```asm
mov rax, 5
```

Artinya:

```text
RAX = 5
```

Register yang sering ditemui:

```text
RAX
RBX
RCX
RDX

RDI
RSI

RSP
RBP

R8
R9
R10
R11
R12
R13
R14
R15
```

---

# 4. RAX, EAX, AX, AL

Mereka bukan register yang sepenuhnya berbeda.

Mereka adalah bagian dari register yang sama:

```text
RAX = 64 bit
EAX = 32 bit
 AX = 16 bit
 AL = 8 bit
```

Contoh:

```asm
mov eax, 5
```

berarti bagian 32-bit dari RAX berisi nilai `5`.

Karena `int` pada C biasanya 32-bit, `EAX`, `EBX`, `ECX`, dan `EDX` sering muncul.

---

# 5. Fungsi Penting RAX / EAX

Pada Linux x86-64, return value sebuah fungsi biasanya berada di:

```text
RAX
```

Untuk return value bertipe `int`, biasanya terlihat sebagai:

```text
EAX
```

Contoh:

```asm
mov eax, 1
ret
```

Kira-kira:

```c
return 1;
```

Contoh:

```asm
xor eax, eax
ret
```

Karena:

```text
x XOR x = 0
```

maka:

```c
return 0;
```

---

# 6. `mov`

Format Intel syntax:

```asm
mov destination, source
```

Contoh:

```asm
mov rax, 5
```

Artinya:

```text
RAX = 5
```

Contoh:

```asm
mov rax, rbx
```

Artinya:

```text
RAX = RBX
```

Ingat:

```text
mov TUJUAN, SUMBER
```

---

# 7. Hexadecimal

Assembly sering menggunakan hexadecimal.

Contoh:

```asm
mov eax, 0x10
```

Artinya:

```text
EAX = 16
```

Beberapa nilai dasar:

```text
0x0  = 0
0x1  = 1
0xA  = 10
0x10 = 16
0x20 = 32
0x2A = 42
0x40 = 64
0xFF = 255
```

Konversi cepat di Linux:

```bash
printf "%d\n" 0x2a
```

Output:

```text
42
```

---

# 8. Memory dan Tanda `[ ]`

Perhatikan perbedaan:

```asm
mov eax, ebx
```

dengan:

```asm
mov eax, [rbx]
```

Misalkan:

```text
RBX = 0x1000

Memory:
0x1000 = 25
```

Maka:

```asm
mov eax, ebx
```

menghasilkan:

```text
EAX = 0x1000
```

Sedangkan:

```asm
mov eax, [rbx]
```

menghasilkan:

```text
EAX = 25
```

Mental model:

```text
rbx
↓
alamat

[rbx]
↓
isi memory pada alamat tersebut
```

Mirip konsep pointer C:

```c
ptr
```

versus:

```c
*ptr
```

---

# 9. BYTE, WORD, DWORD, QWORD

Ukuran data:

```text
BYTE  = 8 bit  = 1 byte
WORD  = 16 bit = 2 byte
DWORD = 32 bit = 4 byte
QWORD = 64 bit = 8 byte
```

Contoh:

```asm
mov eax, DWORD PTR [rbp-0x4]
```

Artinya:

```text
Baca 4 byte dari memory di alamat rbp-0x4,
kemudian masukkan ke EAX.
```

Biasanya data seperti ini merupakan:

```text
int / local variable
```

---

# 10. RSP

```text
RSP = Stack Pointer
```

Menunjuk bagian atas stack.

Stack sering digunakan untuk:

```text
local variable
return address
saved register
function call
```

---

# 11. RBP

```text
RBP = Base Pointer
```

Sering dipakai sebagai referensi stack frame sebuah fungsi.

Contoh:

```asm
push rbp
mov rbp, rsp
sub rsp, 0x20
```

Ini pola umum:

```text
function prologue
```

---

# 12. Function Prologue

Contoh:

```asm
push rbp
mov rbp, rsp
sub rsp, 0x20
```

Makna sederhana:

```text
push rbp
↓
simpan base pointer fungsi sebelumnya

mov rbp, rsp
↓
buat base stack frame baru

sub rsp, 0x20
↓
siapkan 32 byte ruang untuk local variable
```

---

# 13. Stack Frame

Contoh gambaran:

```text
Higher Address

rbp+0x8   → return address
rbp       → saved RBP

rbp-0x4   → local variable
rbp-0x8   → local variable
rbp-0x10  → local variable
rbp-0x20  → local variable

Lower Address
```

Jika melihat:

```asm
[rbp-0x4]
[rbp-0x8]
[rbp-0x10]
```

sering kali itu local variable.

---

# 14. Mental Rename Variable

Assembly:

```asm
mov DWORD PTR [rbp-0x4], 5
mov eax, DWORD PTR [rbp-0x4]
add eax, 3
```

Daripada terus membaca:

```text
[rbp-0x4]
```

anggap saja:

```text
angka
```

Sehingga:

```text
angka = 5
eax = angka
eax += 3
```

Teknik ini sangat membantu saat membaca fungsi panjang.

---

# 15. `add`

```asm
add eax, 5
```

Artinya:

```text
EAX = EAX + 5
```

C:

```c
eax += 5;
```

---

# 16. `sub`

```asm
sub eax, 3
```

Artinya:

```text
EAX = EAX - 3
```

C:

```c
eax -= 3;
```

---

# 17. `imul`

Contoh:

```asm
imul eax, eax, 3
```

Artinya secara sederhana:

```text
EAX = EAX × 3
```

Contoh:

```asm
mov eax, 4
imul eax, eax, 3
```

Hasil:

```text
EAX = 12
```

---

# 18. `xor`

Contoh:

```asm
xor eax, 0x42
```

Artinya:

```text
EAX = EAX XOR 0x42
```

XOR sangat sering dipakai di CTF RE.

Sifat penting:

```text
A XOR B XOR B = A
```

Sehingga operasi XOR dapat dibalik menggunakan key yang sama.

---

# 19. `xor eax, eax`

Pola sangat umum:

```asm
xor eax, eax
```

Karena:

```text
X XOR X = 0
```

maka:

```text
EAX = 0
```

Sering ekuivalen dengan:

```asm
mov eax, 0
```

atau:

```c
return 0;
```

jika berada tepat sebelum `ret`.

---

# 20. `cmp`

Contoh:

```asm
cmp eax, 5
```

Baca sebagai:

```text
Bandingkan EAX dengan 5.
```

Secara internal CPU melakukan operasi seperti:

```text
EAX - 5
```

namun hasilnya tidak disimpan.

Yang berubah adalah flags CPU.

Biasanya `cmp` diikuti conditional jump.

---

# 21. `je`

```text
JE = Jump if Equal
```

Contoh:

```asm
cmp eax, 5
je correct
```

Kira-kira:

```c
if (eax == 5) {
    goto correct;
}
```

---

# 22. `jne`

```text
JNE = Jump if Not Equal
```

Contoh:

```asm
cmp eax, 5
jne wrong
```

Kira-kira:

```c
if (eax != 5) {
    goto wrong;
}
```

Pola ini sangat sering muncul di CTF.

---

# 23. Conditional Jump Penting

```text
je / jz
↓
equal / zero

jne / jnz
↓
not equal / not zero

jg
↓
greater

jl
↓
less

jge
↓
greater or equal

jle
↓
less or equal
```

Contoh:

```asm
cmp eax, 10
jg besar
```

Kira-kira:

```c
if (eax > 10) {
    goto besar;
}
```

---

# 24. `jmp`

```asm
jmp somewhere
```

Merupakan unconditional jump.

Artinya selalu lompat:

```c
goto somewhere;
```

Tidak bergantung pada kondisi.

---

# 25. `test`

Contoh sangat umum:

```asm
test eax, eax
```

Sering digunakan untuk mengecek:

```text
EAX == 0 ?
```

Contoh:

```asm
call check_password
test eax, eax
je wrong
```

Kira-kira:

```c
if (check_password() == 0) {
    goto wrong;
}
```

---

# 26. `test eax, eax`

Secara internal:

```text
EAX AND EAX
```

Jika EAX bernilai zero:

```text
Zero Flag = aktif
```

Maka:

```asm
je wrong
```

akan melakukan jump.

Mental shortcut:

```asm
test eax, eax
je label
```

baca sebagai:

```c
if (eax == 0) {
    goto label;
}
```

---

# 27. `je` vs `jz`

Secara praktis:

```text
JE = Jump if Equal
JZ = Jump if Zero
```

Keduanya mengecek Zero Flag.

Demikian pula:

```text
JNE = Jump if Not Equal
JNZ = Jump if Not Zero
```

---

# 28. `call`

Contoh:

```asm
call check_password
```

Artinya:

```text
Panggil fungsi check_password.
```

Secara konsep:

```text
simpan alamat untuk kembali
↓
lompat ke fungsi
↓
jalankan fungsi
↓
ret
↓
kembali
```

C:

```c
check_password();
```

---

# 29. `ret`

```asm
ret
```

Artinya:

```text
Return dari fungsi.
```

Contoh:

```asm
mov eax, 1
ret
```

Biasanya:

```c
return 1;
```

---

# 30. Calling Convention Linux x86-64

Linux x86-64 umumnya memakai:

```text
System V AMD64 ABI
```

Urutan argument:

```text
Argument 1 → RDI
Argument 2 → RSI
Argument 3 → RDX
Argument 4 → RCX
Argument 5 → R8
Argument 6 → R9
```

Return value:

```text
RAX
```

Ini sangat penting untuk Reverse Engineering.

---

# 31. Versi Register Lebih Kecil untuk Argumen

Jika argument bertipe `int` 32-bit:

```text
RDI → EDI
RSI → ESI
RDX → EDX
RCX → ECX
```

Jika argument hanya 1 byte, kamu mungkin melihat:

```text
DIL
SIL
```

Contoh:

```asm
mov DWORD PTR [rbp-0x4], edi
```

sering berarti:

```c
local_variable = argument_1;
```

---

# 32. Contoh `strcmp`

C:

```c
strcmp(input, secret);
```

Calling convention:

```text
RDI = input
RSI = secret
```

Assembly bisa terlihat:

```asm
lea rax, [rbp-0x40]
lea rsi, [rip+0x1234]
mov rdi, rax
call strcmp
```

Mental translation:

```c
strcmp(input, secret);
```

---

# 33. Return Value `strcmp`

```c
strcmp(a, b)
```

Menghasilkan:

```text
0 → string sama
non-zero → string berbeda
```

Contoh:

```asm
call strcmp
test eax, eax
jne wrong
```

Artinya:

```c
if (strcmp(input, secret) != 0) {
    goto wrong;
}
```

---

# 34. `lea`

```text
LEA = Load Effective Address
```

Contoh:

```asm
lea rax, [rbp-0x40]
```

Artinya:

```text
Ambil alamat rbp-0x40 lalu masukkan ke RAX.
```

Mental shortcut:

```text
lea
↓
ambil ADDRESS
```

---

# 35. `mov` vs `lea`

Misalkan:

```text
rbp-0x40 = address 0x1000

memory 0x1000 = 50
```

Jika:

```asm
mov eax, [rbp-0x40]
```

hasil:

```text
EAX = 50
```

Jika:

```asm
lea rax, [rbp-0x40]
```

hasil:

```text
RAX = 0x1000
```

Shortcut:

```text
mov [memory]
↓
ambil VALUE

lea [memory]
↓
ambil ADDRESS
```

Secara kasar dalam C:

```text
mov → value
lea → &value
```

---

# 36. RIP

```text
RIP = Instruction Pointer
```

Menunjuk lokasi instruksi program saat ini.

Compiler sering memakai:

```text
RIP-relative addressing
```

Contoh:

```asm
lea rdi, [rip+0xe20]
call puts
```

Sering berarti:

```c
puts("suatu string");
```

Karena `[rip+...]` sering mengarah ke:

```text
string
global data
constant
```

---

# 37. `push`

```asm
push rax
```

Artinya secara sederhana:

```text
masukkan RAX ke stack
```

---

# 38. `pop`

```asm
pop rax
```

Artinya:

```text
ambil nilai paling atas stack
↓
masukkan ke RAX
```

---

# 39. Stack = LIFO

```text
LIFO = Last In First Out
```

Contoh:

```asm
push 10
push 20
```

Stack:

```text
20 ← top
10
```

Kemudian:

```asm
pop rax
```

Hasil:

```text
RAX = 20
```

---

# 40. Membaca Fungsi Sederhana

Assembly:

```asm
check:
    push rbp
    mov rbp, rsp

    mov DWORD PTR [rbp-0x4], edi

    cmp DWORD PTR [rbp-0x4], 0x2a
    jne wrong

    mov eax, 1
    jmp end

wrong:
    mov eax, 0

end:
    pop rbp
    ret
```

Interpretasi:

```text
Argument pertama disimpan sebagai local variable.

0x2A = 42.

Jika argument != 42:
    return 0

Jika argument == 42:
    return 1
```

C-like:

```c
int check(int number) {
    if (number == 42) {
        return 1;
    }

    return 0;
}
```

---

# 41. Mengenali `if`

Pola:

```asm
cmp eax, 5
jne wrong
```

Berarti jalur sukses hanya terjadi jika:

```text
EAX == 5
```

C-like:

```c
if (eax != 5) {
    goto wrong;
}
```

---

# 42. Mengenali `if-else`

Contoh:

```asm
cmp eax, 5
jne else_part

mov ebx, 1
jmp end

else_part:
mov ebx, 0

end:
```

C-like:

```c
if (eax == 5) {
    ebx = 1;
} else {
    ebx = 0;
}
```

---

# 43. Mengenali Loop

Pola:

```asm
loop:
    ...
    add eax, 1
    cmp eax, 10
    jl loop
```

Karena ada jump kembali ke alamat sebelumnya:

```text
loop
 ↑  ↓
 └──┘
```

kemungkinan merupakan:

```c
for (...)
```

atau:

```c
while (...)
```

Shortcut:

```text
jump ke belakang
↓
kemungkinan loop
```

---

# 44. Character Comparison

Misalnya:

```asm
movzx eax, BYTE PTR [rax]
cmp al, 0x41
jne wrong
```

Karena:

```text
0x41 = 'A'
```

kemungkinan program mengecek:

```c
if (input[...] != 'A') {
    goto wrong;
}
```

---

# 45. ASCII Penting

Beberapa nilai yang bagus dikenali:

```text
'A' = 0x41
'Z' = 0x5A

'a' = 0x61
'z' = 0x7A

'0' = 0x30
'9' = 0x39
```

Minimal ingat:

```text
0x41 → A
0x61 → a
0x30 → 0
```

---

# 46. `movzx`

Contoh:

```asm
movzx eax, BYTE PTR [rax]
```

Artinya:

```text
ambil 1 byte
↓
masukkan ke EAX
↓
isi bit sisanya dengan 0
```

Sering muncul saat program membaca:

```c
char
input[i]
```

---

# 47. Array / String Access

Satu baris C seperti:

```c
input[i]
```

bisa menghasilkan banyak assembly:

```asm
mov eax, DWORD PTR [rbp-0x4]
movsxd rdx, eax
mov rax, QWORD PTR [rbp-0x18]
add rax, rdx
movzx eax, BYTE PTR [rax]
```

Jangan menerjemahkan assembly satu instruksi = satu baris C.

Cari pola keseluruhan:

```text
ambil i
↓
hitung alamat input[i]
↓
ambil satu byte
```

Artinya secara konsep:

```c
input[i]
```

---

# 48. Pola Validasi CTF

Saat membaca challenge, cari flow:

```text
INPUT
  ↓
TRANSFORM
  ↓
COMPARE
  ↓
CONDITIONAL JUMP
  ↓
SUCCESS / FAIL
```

Contoh:

```asm
movzx eax, BYTE PTR [...]
xor eax, 0x23
cmp eax, 0x62
jne wrong
```

Interpretasi:

```text
input XOR 0x23 harus sama dengan 0x62
```

Maka:

```text
input = 0x62 XOR 0x23
```

---

# 49. Contoh Reverse XOR

Jika:

```text
input XOR 0x23 = 0x62
```

Karena XOR reversible:

```text
input = 0x62 XOR 0x23
```

Python:

```python
print(hex(0x62 ^ 0x23))
print(chr(0x62 ^ 0x23))
```

Hasil:

```text
0x41
A
```

Jadi input:

```text
A
```

---

# 50. Workflow Membaca Assembly

Ketika membuka fungsi, cari:

```text
1. Input masuk dari mana?
2. Input disimpan di mana?
3. Input mengalami operasi apa?
4. Dibandingkan dengan apa?
5. Jump apa yang menentukan success/fail?
6. Fungsi apa yang dipanggil pada jalur success?
```

Biasanya target utama:

```text
scanf
fgets
read
strcmp
strncmp
memcmp
cmp
test
je
jne
win
flag
correct
wrong
```

---

# 51. Jangan Membaca Assembly Seperti Novel

Kesalahan umum:

```text
"Saya harus memahami instruksi pertama."
"Saya harus memahami instruksi kedua."
"Saya harus memahami semuanya."
```

Lebih baik:

```text
Function prologue
↓
skip cepat

Input
↓
focus

Loop / transform
↓
focus

Compare
↓
VERY FOCUS

printf biasa
↓
skip jika tidak penting
```

Reverse Engineering juga berarti:

```text
filtering information
```

---

# 52. Assembly → C Cheat Mapping

## Assignment

```asm
mov eax, 5
```

```c
eax = 5;
```

---

## Addition

```asm
add eax, 2
```

```c
eax += 2;
```

---

## Subtraction

```asm
sub eax, 2
```

```c
eax -= 2;
```

---

## XOR

```asm
xor eax, 0x42
```

```c
eax ^= 0x42;
```

---

## Equal

```asm
cmp eax, 5
je correct
```

```c
if (eax == 5) {
    goto correct;
}
```

---

## Not Equal

```asm
cmp eax, 5
jne wrong
```

```c
if (eax != 5) {
    goto wrong;
}
```

---

## Zero Check

```asm
test eax, eax
je wrong
```

```c
if (eax == 0) {
    goto wrong;
}
```

---

## Function Call

```asm
call check
```

```c
check(...);
```

---

## Return 1

```asm
mov eax, 1
ret
```

```c
return 1;
```

---

## Return 0

```asm
xor eax, eax
ret
```

```c
return 0;
```

---

# 53. Register Cheat Sheet

```text
RAX
↓
return value / temporary calculation

RDI
↓
argument 1

RSI
↓
argument 2

RDX
↓
argument 3

RCX
↓
argument 4

R8
↓
argument 5

R9
↓
argument 6

RSP
↓
stack pointer

RBP
↓
stack-frame reference

RIP
↓
instruction pointer
```

---

# 54. Size Cheat Sheet

```text
RAX = 64 bit
EAX = 32 bit
 AX = 16 bit
 AL = 8 bit
```

```text
BYTE  = 1 byte
WORD  = 2 byte
DWORD = 4 byte
QWORD = 8 byte
```

---

# 55. Branch Cheat Sheet

```text
jmp
↓
selalu lompat

je / jz
↓
equal / zero

jne / jnz
↓
not equal / not zero

jg
↓
greater

jl
↓
less

jge
↓
greater or equal

jle
↓
less or equal
```

---

# 56. Function Cheat Sheet

```text
call
↓
masuk ke fungsi

ret
↓
kembali dari fungsi

RDI
↓
argumen pertama

RSI
↓
argumen kedua

RDX
↓
argumen ketiga

RAX
↓
return value
```

---

# 57. Memory Cheat Sheet

```text
rax
↓
nilai/alamat yang tersimpan di register

[rax]
↓
isi memory pada alamat RAX

lea rax, [something]
↓
ambil alamat

mov eax, [something]
↓
ambil isi memory
```

---

# 58. Pola `strcmp`

```asm
mov rdi, ...
mov rsi, ...
call strcmp
test eax, eax
jne wrong
```

Mental translation:

```c
if (strcmp(arg1, arg2) != 0) {
    goto wrong;
}
```

Jika jump-nya:

```asm
je correct
```

maka string sama akan menuju `correct`.

---

# 59. Pola Return Boolean

```asm
cmp ...
jne wrong

mov eax, 1
jmp end

wrong:
xor eax, eax

end:
ret
```

Mental translation:

```c
if (condition) {
    return 1;
}

return 0;
```

---

# 60. Pola CTF yang Sangat Umum

```text
input
↓
strlen
↓
cek panjang
↓
loop setiap karakter
↓
XOR / ADD / SUB
↓
compare dengan array target
↓
jika semua benar
↓
win
```

Saat melihat assembly panjang, coba cari pola ini daripada membaca semuanya secara literal.

---

# 61. Contoh Mini Challenge

Assembly:

```asm
check:
    push rbp
    mov rbp, rsp

    mov DWORD PTR [rbp-0x4], edi

    mov eax, DWORD PTR [rbp-0x4]
    imul eax, eax, 0x3
    add eax, 0x5

    cmp eax, 0x23
    jne wrong

    mov eax, 1
    jmp finish

wrong:
    mov eax, 0

finish:
    pop rbp
    ret
```

Analisis:

```text
input disimpan

input × 3

hasil + 5

dibandingkan dengan 0x23
```

Karena:

```text
0x23 = 35
```

Syarat:

```text
input × 3 + 5 = 35
```

Balik:

```text
input × 3 = 30

input = 10
```

Jadi:

```text
check(10)
```

akan menghasilkan:

```text
return 1
```

---

# 62. Mental Model Utama RE #2

Jangan lihat assembly sebagai kumpulan instruksi asing.

Lihat sebagai:

```text
VALUE / INPUT
     ↓
DISIMPAN
     ↓
DIMODIFIKASI
     ↓
DIBANDINGKAN
     ↓
BRANCH
     ↓
SUCCESS / FAIL
```

Pertanyaan utama:

```text
Apa nilai awalnya?

Di mana disimpan?

Operasi apa yang dilakukan?

Dibandingkan dengan apa?

Jump mana yang menuju fail?

Syarat apa yang membuat program menuju success?
```

---

# 63. Prioritas Saat Membaca Assembly

Fokus tinggi:

```text
call
cmp
test
je
jne
jg
jl
xor
add
sub
imul
```

Perhatikan:

```text
RDI
RSI
RDX
RAX
```

karena sangat berkaitan dengan function argument dan return value.

Tidak perlu terlalu lama pada:

```text
function prologue
function epilogue
compiler boilerplate
```

jika belum relevan dengan logika challenge.

---

# 64. Checklist RE #2

Setelah belajar materi ini, usahakan bisa menjawab:

```text
1. Apa fungsi RAX?

2. Apa fungsi RDI dan RSI?

3. Apa bedanya RAX dengan EAX?

4. Apa arti tanda []?

5. Apa bedanya mov dan lea?

6. Apa fungsi RSP?

7. Apa fungsi RBP?

8. Apa arti cmp?

9. Apa arti test eax,eax?

10. Apa beda je dan jne?

11. Apa fungsi call?

12. Apa fungsi ret?

13. Bagaimana return value dikirim?

14. Bagaimana argument fungsi dikirim?

15. Bagaimana mengenali if?

16. Bagaimana mengenali loop?

17. Bagaimana mengenali pengecekan karakter?

18. Bagaimana mengenali pola XOR?

19. Bagaimana menerjemahkan assembly menjadi C-like?

20. Bagaimana menemukan kondisi menuju jalur success?
```

---

# 65. Cheat Sheet Super Singkat

```text
mov dst, src
→ dst = src

lea dst, [x]
→ dst = address x

[x]
→ isi memory pada alamat x

add a, b
→ a += b

sub a, b
→ a -= b

imul a, a, b
→ a *= b

xor a, b
→ a ^= b

cmp a, b
→ bandingkan a dengan b

test eax, eax
→ cek apakah eax == 0

jmp
→ selalu lompat

je / jz
→ lompat jika equal / zero

jne / jnz
→ lompat jika tidak equal / tidak zero

call
→ panggil fungsi

ret
→ keluar dari fungsi
```

Calling convention:

```text
RDI → argument 1
RSI → argument 2
RDX → argument 3
RCX → argument 4
R8  → argument 5
R9  → argument 6

RAX → return value
```

Stack:

```text
RSP → stack pointer
RBP → stack-frame reference
```

---

# 66. Prinsip Penting RE #2

Target belajar assembly untuk Reverse Engineering bukan:

```text
"Hafal seluruh x86-64."
```

Tetapi:

```text
"Mampu mengikuti data dan control flow."
```

Terutama pola:

```text
input
↓
transform
↓
compare
↓
conditional jump
↓
correct / wrong
```

Jika pola tersebut sudah mulai mudah dibaca, kamu sudah siap masuk ke:

```text
RE #3 — Ghidra untuk Reverse Engineering CTF
```

Pada RE #3 fokus berikutnya adalah:

```text
main
Defined Strings
XREF
Decompiler
Listing
rename function
rename variable
follow function call
mencocokkan C-like code dengan assembly
menganalisis check_password
```
