def enkripsi(teks, kunci):
    hasil = ""
    kunci = kunci.upper()
    index_kunci = 0

    for karakter in teks:
        if karakter.isalpha():
            basis = ord('A') if karakter.isupper() else ord('a')

            p = ord(karakter.upper()) - ord('A')
            k = ord(kunci[index_kunci % len(kunci)]) - ord('A')

            c = (p + k) % 26

            hasil += chr(c + basis)
            index_kunci += 1
        else:
            hasil += karakter

    return hasil


def dekripsi(teks, kunci):
    hasil = ""
    kunci = kunci.upper()
    index_kunci = 0

    for karakter in teks:
        if karakter.isalpha():
            basis = ord('A') if karakter.isupper() else ord('a')

            c = ord(karakter.upper()) - ord('A')
            k = ord(kunci[index_kunci % len(kunci)]) - ord('A')

            p = (c - k) % 26

            hasil += chr(p + basis)
            index_kunci += 1
        else:
            hasil += karakter

    return hasil


while True:
    print("\n=== VIGENERE CIPHER ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        plaintext = input("Masukkan plaintext: ")
        kunci = input("Masukkan kata kunci: ")

        if not kunci.isalpha():
            print("Kunci harus berupa huruf!")
            continue

        hasil = enkripsi(plaintext, kunci)

        print("Ciphertext :", hasil)

    elif pilihan == "2":
        ciphertext = input("Masukkan ciphertext: ")
        kunci = input("Masukkan kata kunci: ")

        if not kunci.isalpha():
            print("Kunci harus berupa huruf!")
            continue

        hasil = dekripsi(ciphertext, kunci)

        print("Plaintext :", hasil)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")