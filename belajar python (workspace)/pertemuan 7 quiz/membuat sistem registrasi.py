
import json
import os
import re

FILE_DATA = "data_diri.json"


def baca_data():
    if not os.path.exists(FILE_DATA):
        return []

    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def registrasi():
    print("\n========== REGISTRASI DATA DIRI ==========")

    nama = input("Nama lengkap       : ").strip()
    nim = input("NIM / ID           : ").strip()
    tempat_lahir = input("Tempat lahir       : ").strip()
    tanggal_lahir = input("Tanggal lahir      : ").strip()
    jenis_kelamin = input("Jenis kelamin      : ").strip()
    email = input("Email              : ").strip()
    program_studi = input("Program studi      : ").strip()
    alamat = input("Alamat             : ").strip()
    hobi = input("Hobi               : ").strip()
    tentang_saya = input("Tentang diri saya  : ").strip()

    if not nama or not nim or not email:
        print("\nNama, NIM/ID, dan email wajib diisi!")
        return

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print("\nFormat email tidak valid!")
        return

    data = baca_data()

    for pengguna in data:
        if pengguna["nim"] == nim:
            print("\nNIM/ID sudah terdaftar!")
            return

    pengguna_baru = {
        "nama": nama,
        "nim": nim,
        "tempat_lahir": tempat_lahir,
        "tanggal_lahir": tanggal_lahir,
        "jenis_kelamin": jenis_kelamin,
        "email": email,
        "program_studi": program_studi,
        "alamat": alamat,
        "hobi": hobi,
        "tentang_saya": tentang_saya
    }

    data.append(pengguna_baru)
    simpan_data(data)

    print("\nRegistrasi berhasil!")
    tampilkan_profil(pengguna_baru)


def tampilkan_profil(pengguna):
    print("\n" + "=" * 45)
    print("             PROFIL DATA DIRI")
    print("=" * 45)
    print(f"Nama lengkap  : {pengguna['nama']}")
    print(f"NIM / ID      : {pengguna['nim']}")
    print(f"Tempat lahir  : {pengguna['tempat_lahir']}")
    print(f"Tanggal lahir : {pengguna['tanggal_lahir']}")
    print(f"Jenis kelamin : {pengguna['jenis_kelamin']}")
    print(f"Email         : {pengguna['email']}")
    print(f"Program studi : {pengguna['program_studi']}")
    print(f"Alamat        : {pengguna['alamat']}")
    print(f"Hobi          : {pengguna['hobi']}")
    print(f"Tentang saya  : {pengguna['tentang_saya']}")
    print("=" * 45)


def lihat_data():
    print("\n========== LIHAT DATA DIRI ==========")
    nim = input("Masukkan NIM/ID terdaftar: ").strip()

    data = baca_data()

    for pengguna in data:
        if pengguna["nim"] == nim:
            tampilkan_profil(pengguna)
            return

    print("\nData tidak ditemukan. Silakan registrasi terlebih dahulu.")


def menu():
    while True:
        print("\n===================================")
        print("       APLIKASI REGISTRASI")
        print("            DATA DIRI")
        print("===================================")
        print("1. Registrasi data diri")
        print("2. Tampilkan data diri")
        print("3. Keluar")
        print("===================================")

        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-3.")


if __name__ == "__main__":
    menu()
