nama = input("Masukkan nama Mahasiswa:")
nilai = float(input("Masukkan Niali Mahasiswa:"))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")

elif nilai>=85:
    print("Nama:",nama)
    print ("Status:Lulus")
    print ("Prediksi:A")
elif nilai>=75:
    print("Nama:",nama)
    print ("Status:Lulus")
    print ("Prediksi:B")
elif nilai>=60:
    print("Nama:",nama)
    print ("Status:Lulus")
    print ("Prediksi:C")
else:
    print("Nama:",nama)
    print ("Status:Tidak Lulus")
    print ("Prediksi:D")



angka = 0

while angka<10:
    angka+=1

    if angka %2 ==0:
        continue
    print (angka)

    buah = ["Apel","Jeruk","Mangga"]
    buah.append("Pisang")
    buah[0]="Anggur"
    print(buah)