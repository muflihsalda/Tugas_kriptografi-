def enkripsi(teks, kunci):
    hasil = ""

    for karakter in teks:
        if karakter.isalpha():
            basis = ord('A') if karakter.isupper() else ord('a')
            hasil += chr((ord(karakter) - basis + kunci) % 26 + basis)
        else:
            hasil += karakter

    return hasil


def dekripsi(teks, kunci):
    return enkripsi(teks, -kunci)


while True:
    print("\n=== CAESAR CIPHER ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        plaintext = input("Masukkan plaintext: ")
        kunci = int(input("Masukkan kunci/pergeseran (0-25): "))

        hasil = enkripsi(plaintext, kunci)

        print("Ciphertext :", hasil)

    elif pilihan == "2":
        ciphertext = input("Masukkan ciphertext: ")
        kunci = int(input("Masukkan kunci/pergeseran (0-25): "))

        hasil = dekripsi(ciphertext, kunci)

        print("Plaintext :", hasil)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")