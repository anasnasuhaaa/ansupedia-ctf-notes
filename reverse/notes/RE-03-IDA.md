# RE #3 — IDA untuk CTF (Ringkas)

Tujuan RE #3:

> Jangan membaca semua function. Cari jalur yang relevan menuju `success`, `correct`, `win`, atau flag.

---

# 1. Workflow Utama

Jangan pakai pola:

```text
Buka IDA
↓
F5
↓
Baca semua pseudocode
↓
Pusing
```

Pakai:

```text
Binary
↓
Cari clue
↓
Strings / Imports / main
↓
XREF
↓
Function penting
↓
Rename
↓
Baca pseudocode
↓
Cek assembly jika perlu
↓
Cari syarat success
```

---

# 2. Shortcut yang Cukup Dihafal

```text
F5
→ Decompile function

Tab
→ Pseudocode ↔ Assembly

X
→ XREF / siapa yang memakai ini?

N
→ Rename

Shift + F12
→ Strings

Shift + F3
→ Functions

Space
→ Graph View ↔ Linear View

Esc
→ Kembali ke posisi sebelumnya

G
→ Lompat ke address
```

Untuk sekarang cukup ini.

---

# 3. Strings = Jalan Masuk Paling Mudah

Buka:

```text
Shift + F12
```

Cari string seperti:

```text
Correct
Wrong
Password
Success
Flag
Congratulations
Invalid
Accepted
```

Misalnya ada:

```text
"Correct!"
```

Klik string tersebut lalu tekan:

```text
X
```

Tujuannya:

```text
Cari function yang menggunakan "Correct!"
```

Ini jauh lebih cepat daripada membaca ratusan function.

---

# 4. XREF Sangat Penting

```text
XREF = Cross Reference
```

Gunanya:

```text
"Siapa yang memakai function/string/data ini?"
```

Contoh:

```text
"Correct!"
↓ XREF
sub_401200
```

Masuk ke:

```text
sub_401200
```

Lalu:

```text
F5
```

---

# 5. Jangan Takut Nama `sub_...`

Contoh:

```text
sub_401230
sub_401350
sub_401500
```

Itu hanya nama sementara dari IDA.

Kalau sudah tahu fungsinya:

```text
sub_401230
↓
check_input
```

Tekan:

```text
N
```

untuk rename.

---

# 6. Rename Itu Penting

Awalnya:

```c
if (sub_401230(v4))
{
    sub_401500();
}
```

Setelah rename:

```c
if (check_input(input))
{
    win();
}
```

Jauh lebih mudah dibaca.

Rename juga variable:

```text
v4
↓
input

v5
↓
index

v6
↓
length
```

---

# 7. Jangan Baca Semua Function

Kalau binary punya:

```text
300 function
```

bukan berarti harus membaca 300.

Bisa jadi jalur penting hanya:

```text
main
↓
read_input
↓
check_input
↓
transform
↓
win
```

Fokus hanya pada jalur tersebut.

---

# 8. Cara Membaca Function Panjang

Jangan baca baris 1 sampai terakhir.

Cari dulu:

```text
return 0
return 1
strcmp
memcmp
strlen
cmp
if
loop
```

Misalnya:

```c
if (strlen(input) != 8)
    return 0;

if (input[0] != 'A')
    return 0;

if ((input[1] ^ 0x23) != target[1])
    return 0;

return 1;
```

Baca sebagai:

```text
Constraint 1:
panjang harus 8

Constraint 2:
input[0] harus 'A'

Constraint 3:
input[1] XOR 0x23 harus sama dengan target[1]

Jika semua benar:
return 1
```

---

# 9. Fokus pada Success Path

Selalu tanyakan:

```text
Apa syarat supaya program tidak masuk `wrong`?

Apa syarat supaya return value = 1?

Apa syarat supaya function `win` dipanggil?
```

Jangan terlalu fokus pada kode yang tidak berhubungan dengan success.

---

# 10. Pseudocode vs Assembly

Gunakan:

```text
F5
```

untuk membaca pseudocode.

Kalau ada bagian membingungkan:

```text
Tab
```

lihat assembly.

Contoh pseudocode:

```c
if (check_input(input))
    win();
```

Assembly:

```asm
call check_input
test eax, eax
je wrong
call win
```

Artinya:

```text
check_input dipanggil

hasil return ada di EAX

jika EAX == 0
→ wrong

jika bukan 0
→ win
```

---

# 11. Assembly Tidak Perlu Dibaca Semua

Gunakan assembly hanya jika:

```text
Pseudocode membingungkan

Kondisi if tidak jelas

Ingin tahu argument function

Ingin memastikan jump

Decompiler terlihat aneh
```

Jadi:

```text
Pseudocode
→ utama

Assembly
→ verifikasi
```

---

# 12. Graph View

Tekan:

```text
Space
```

untuk melihat Graph View.

Berguna jika function punya banyak:

```text
if
else
loop
jump
```

Mental model:

```text
        condition
        /      \
      yes      no
       |        |
    success    fail
```

Tidak wajib selalu dipakai.

---

# 13. Imports Bisa Jadi Clue

Cari import seperti:

```text
strcmp
strncmp
memcmp
strlen
scanf
fgets
read
puts
printf
```

Contoh:

```text
strcmp
```

bisa memberi clue:

```text
program membandingkan string
```

Kalau perlu, gunakan XREF untuk melihat siapa yang memanggil `strcmp`.

---

# 14. Pola Challenge yang Sering Muncul

```text
input
↓
cek panjang
↓
loop karakter
↓
XOR / ADD / SUB
↓
compare dengan target
↓
jika salah → return 0
↓
jika semua benar → return 1
```

Kalau melihat pola ini, jangan baca sebagai 50 baris kode.

Ringkas menjadi:

```text
input ditransform lalu dibandingkan dengan target
```

---

# 15. Contoh

Pseudocode:

```c
bool check_input(char *input)
{
    int i;

    if (strlen(input) != 8)
        return 0;

    for (i = 0; i < 8; i++)
    {
        if ((input[i] ^ 0x23) != target[i])
            return 0;
    }

    return 1;
}
```

Yang perlu dipahami hanya:

```text
panjang input = 8

untuk setiap karakter:

input[i] XOR 0x23
harus sama dengan
target[i]
```

Maka:

```text
input[i] = target[i] XOR 0x23
```

Selesai.

---

# 16. Mental Checklist Saat Pakai IDA

Tanyakan:

```text
1. Ada string success/fail?

2. String itu dipakai oleh function mana?

3. Function itu menerima input dari mana?

4. Function validasinya mana?

5. Apa syarat return 1?

6. Apa transformasi terhadap input?

7. Dibandingkan dengan apa?

8. Function mana yang dipanggil saat success?
```

Kalau sudah terjawab, biasanya tidak perlu membaca function lain.

---

# 17. Shortcut Super Ringkas

```text
F5
→ Decompile

X
→ XREF

N
→ Rename

Tab
→ Pseudocode / Assembly

Shift+F12
→ Strings

Shift+F3
→ Functions

Space
→ Graph View

Esc
→ Back
```

---

# 18. Prinsip Utama RE #3

Jangan berpikir:

```text
"Saya harus memahami seluruh binary."
```

Pikirkan:

```text
"Saya hanya perlu memahami bagian
yang menentukan jalur menuju success."
```

Workflow paling penting:

```text
Strings
↓
XREF
↓
Function penting
↓
Rename
↓
Pseudocode
↓
Assembly jika perlu
↓
Cari constraint
↓
Reverse algoritma
↓
Flag
```

---

# 19. Target Setelah RE #3

Minimal kamu mampu:

```text
mencari string menarik

menggunakan XREF

menemukan function penting

rename function/variable

mengabaikan function tidak relevan

membaca pseudocode sebagai constraint

memakai assembly hanya saat perlu

mengikuti jalur menuju success
```

Jika ini sudah nyaman, baru lanjut ke:

```text
RE #4 — Debugging dengan GDB / IDA Debugger
```
