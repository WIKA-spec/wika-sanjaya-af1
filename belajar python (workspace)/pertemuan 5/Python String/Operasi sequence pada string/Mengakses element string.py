text = "hello python"
print(text[0])

#Selain via index, keyword perulangan for bisa dimanfaatkan untuk mengiterasi elemen string. Contoh:

for c in text:
    print(c)

#Contoh lain menggunakan range() :

for i in range(0, len(text)):
    print(text[i])