profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
    }

#Ok, sekarang dari kode di atas, coba tambahkan kode berikut
# untuk melihat bagaimana data dictionary dimunculkan di layar console.

print("data:", profile)
print("total keys:", len(profile))

#Sedangkan untuk memunculkan nilai item tertentu berdasarkan key-nya,
# bisa dilakukan menggunakan notasi dict["key"] . Contoh:

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])