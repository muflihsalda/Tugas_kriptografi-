# Tugas_kriptografi-

# 3 Aplikasi Cipher Klasik Menggunakan Python

## Deskripsi

Project ini berisi tiga aplikasi sederhana untuk melakukan enkripsi dan dekripsi menggunakan algoritma kriptografi klasik.

Aplikasi dibuat menggunakan bahasa pemrograman Python dan dijalankan melalui terminal/command prompt.

Tiga algoritma yang digunakan:

1. Caesar Cipher
2. Vigenère Cipher
3. Columnar Transposition Cipher

Project ini dibuat berdasarkan materi Kriptografi tentang cipher klasik.

---

## 1. Caesar Cipher

Caesar Cipher merupakan cipher substitusi yang melakukan pergeseran setiap huruf alfabet berdasarkan nilai kunci.

### Rumus

Enkripsi:

`C = (P + K) mod 26`

Dekripsi:

`P = (C - K) mod 26`

### Contoh

Plaintext:

`HALO`

Kunci:

`3`

Ciphertext:

`K D O R`

### Menjalankan Program

```bash
python caesar_cipher.py
```

---

## 2. Vigenère Cipher

Vigenère Cipher merupakan cipher abjad-majemuk. Setiap huruf plaintext dienkripsi menggunakan nilai kunci yang berbeda secara berulang.

### Contoh

Plaintext:

`HALO DUNIA`

Kunci:

`KEY`

Program akan menggunakan kunci secara berulang sampai seluruh plaintext selesai diproses.

### Menjalankan Program

```bash
python vigenere_cipher.py
```

---

## 3. Columnar Transposition Cipher

Columnar Transposition Cipher merupakan cipher transposisi yang mengubah posisi atau susunan karakter plaintext berdasarkan kolom dan kata kunci.

Pada proses enkripsi, plaintext dimasukkan ke dalam tabel berdasarkan panjang kunci. Selanjutnya karakter dibaca berdasarkan urutan alfabet dari kata kunci.

### Contoh

Plaintext:

`SISTEM DAN TEKNOLOGI`

Kunci:

`TOMBAK`

Program akan menyusun plaintext ke dalam tabel kemudian membaca kolom berdasarkan urutan huruf pada kunci.

### Menjalankan Program

```bash
python columnar_transposition.py
```

---

## Struktur Project

```text
3-aplikasi-cipher/
│
├── caesar-cipher/
│   └── caesar_cipher.py
│
├── vigenere-cipher/
│   └── vigenere_cipher.py
│
├── columnar-transposition/
│   └── columnar_transposition.py
│
└── README.md
```

---

## Cara Menjalankan

Pastikan Python sudah terinstall.

Cek Python dengan:

```bash
python --version
```

Kemudian masuk ke folder aplikasi yang ingin dijalankan.

Contoh:

```bash
cd caesar-cipher
python caesar_cipher.py
```

Program akan menampilkan menu:

```text
1. Enkripsi
2. Dekripsi
3. Keluar
```

---

## Tujuan

Project ini bertujuan untuk memahami konsep dasar kriptografi klasik, khususnya proses enkripsi dan dekripsi menggunakan cipher substitusi dan cipher transposisi.

## Teknologi

* Python
* Terminal / Command Prompt
* Git & GitHub

## Catatan

Cipher klasik digunakan untuk pembelajaran konsep dasar kriptografi dan bukan untuk mengamankan data sensitif pada sistem modern.
