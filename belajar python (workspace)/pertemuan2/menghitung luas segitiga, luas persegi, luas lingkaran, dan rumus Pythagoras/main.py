import math

print("===================================")
print(" PROGRAM MENGHITUNG RUMUS BANGUN")
print("===================================")
print("1. Luas Segitiga")
print("2. Luas Persegi")
print("3. Luas Lingkaran")
print("4. Pythagoras")
print("===================================")

pilihan = int(input("Masukkan pilihan (1-4): "))

if pilihan == 1:
    print("\n=== LUAS SEGITIGA ===")
    alas = float(input("Masukkan alas : "))
    tinggi = float(input("Masukkan tinggi : "))
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga =", luas)

elif pilihan == 2:
    print("\n=== LUAS PERSEGI ===")
    sisi = float(input("Masukkan panjang sisi : "))
    luas = sisi * sisi
    print("Luas Persegi =", luas)

elif pilihan == 3:
    print("\n=== LUAS LINGKARAN ===")
    jari = float(input("Masukkan jari-jari : "))
    luas = math.pi * jari * jari
    print("Luas Lingkaran =", luas)

elif pilihan == 4:
    print("\n=== PYTHAGORAS ===")
    alas = float(input("Masukkan sisi alas : "))
    tinggi = float(input("Masukkan sisi tinggi : "))
    miring = math.sqrt((alas ** 2) + (tinggi ** 2))
    print("Panjang sisi miring =", miring)

else:
    print("Pilihan tidak tersedia.")