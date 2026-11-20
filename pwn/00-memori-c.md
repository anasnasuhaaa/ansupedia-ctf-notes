# Dari objek C ke alamat memori

**Tujuan.** Prediksi ukuran objek, bedakan panjang string dari kapasitas array, dan tentukan kapan pointer masih sah dipakai. Bekal awalnya adalah kemampuan mengompilasi [contoh jumlah](README.md#siapkan-program-latihan).

Simpan sebagai `objek.c` di direktori latihan. Program membuat salinan milik pemanggil. Argumen panjang mencakup terminator.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char label[] = "ELF";

static char *salin(const char *asal, size_t ukuran) {
    char *hasil = malloc(ukuran);
    if (hasil != NULL)
        memcpy(hasil, asal, ukuran);
    return hasil;
}

int main(void) {
    char lokal[] = "ELF";
    char *milik = salin(lokal, sizeof lokal);
    if (milik == NULL)
        return 1;
    milik[0] = 'e';
    printf("%s %s %s\n", label, lokal, milik);
    printf("array=%zu panjang=%zu pointer=%zu\n",
           sizeof lokal, strlen(lokal), sizeof milik);
    free(milik);
    return 0;
}
```

Di shell, pisahkan langkah kompilasi dan penautan agar artefaknya bisa dibandingkan.

```sh
gcc -std=c17 -Wall -Wextra -g -O0 -c objek.c -o objek.o
readelf -hW objek.o
nm -u objek.o
gcc objek.o -o objek
./objek
```

Objek bertipe `REL` masih mengandung rujukan seperti `malloc` yang harus ditangani saat penautan/pemuatan. Baris pertama program semestinya berbunyi `ELF ELF eLF`: salinan memiliki penyimpanan sendiri. Pada ABI Linux x86-64 LP64, baris kedua memberi 4, 3, 8. Empat byte array mencakup karakter nol; `strlen` membaca sampai karakter nol pertama. Pointer menyimpan alamat, sehingga `sizeof milik` mengukur pointer. Dalam parameter fungsi, deklarasi `char asal[]` juga menjadi pointer. Sertakan panjang yang diketahui pemanggil.

| Objek | Masa hidup dan tempat yang lazim terlihat | Tanggung jawab |
| --- | --- | --- |
| `label` | Sepanjang program, data konstan sering di .rodata | Boleh dibaca selama program hidup |
| `lokal`, variabel pointer `milik` | Sampai blok di main selesai; build debug biasanya menaruhnya di frame stack | Alamat elemen lokal sah selama objek hidup |
| Byte yang ditunjuk `milik` | Sejak alokasi berhasil sampai free; allocator mengelola penyimpanannya | Pemanggil menjadi pemilik setelah salin mengembalikan hasil dan membebaskannya sekali |

Kontrak `salin` mensyaratkan sedikitnya `ukuran` byte sumber dapat dibaca. Di sini `sizeof lokal` membuktikan syarat itu; ukuran dari masukan pengguna memerlukan validasi terpisah. Membaca melewati objek, memakai alias setelah `free`, atau memodifikasi literal string menimbulkan *undefined behavior*. Hasil yang terlihat benar dalam satu percobaan tidak menjamin eksekusi berikutnya.

Untuk input teks, sediakan array nyata, misalnya `char baris[32]`, lalu periksa apakah `fgets(baris, sizeof baris, stdin)` berhasil. Periksa juga newline untuk membedakan baris lengkap dan potongan. Pemakaian `gets` atau `scanf("%s", baris)` tanpa batas tidak menjaga kapasitas. Untuk data biner gunakan jumlah byte eksplisit; nol dapat menjadi bagian data.

**Uji diri.** Bila isi awal berubah menjadi `"ELF64"`, apa yang berubah pada tiga ukuran tadi? Berapa byte yang dapat dibaca dengan aman melalui `milik` sesudah `free`? Jelaskan mengapa mengembalikan alamat array otomatis dari fungsi pembuatnya gagal memenuhi kontrak kepemilikan.

**Ringkas.** Ukuran, panjang, dan masa hidup adalah tiga fakta terpisah. Ikuti objeknya ketika membaca [segmen ELF](01-elf.md) dan ikuti nilai pointer melalui [register argumen](03-abi.md).
