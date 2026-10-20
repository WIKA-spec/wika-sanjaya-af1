name = "Aiden Pearce"
occupation = "IT support"
text = f"hello, my name is {name}, I'm an {occupation}"
print(text)

#Selain menggunakan metode di atas, ada beberapa alternatif cara lain yang bisa digunakan, diantaranya:

text = "hello, my name is {name}, I'm an {occupation}".format(name = name, occupation = occupation)
print(text)

text = "hello, my name is {0}, I'm an {1}".format(name, occupation)
print(text)

text = "hello, my name is {}, I'm an {}".format(name, occupation)
print(text)