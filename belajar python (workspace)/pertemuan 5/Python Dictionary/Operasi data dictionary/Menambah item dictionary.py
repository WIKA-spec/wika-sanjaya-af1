profile = {
    "name": "mario",
    }
print("len:", len(profile), "data:", profile)

profile["favourite_color"] = "red"
print("len:", len(profile), "data:", profile)

#Selain cara tersebut, bisa juga dengan menggunakan method update().
# Tulis key dan value baru yang ingin ditambahkan sebagai argument method update() dalam bentuk dictionary.

profile.update({"race": "italian"})
print("len:", len(profile), "data:", profile)