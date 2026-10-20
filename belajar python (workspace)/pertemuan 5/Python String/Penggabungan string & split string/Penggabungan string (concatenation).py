#Menggunakan teknik penulisan string literal sebaris
text = "hello " "python"
print(text)

#Menggunakan operator +
text_one = "hello"
text_two = "python"
text = text_one + " " + text_two
print(text)

#Untuk data non-string jika ingin digabung harus dibungkus
# dengan fungsi str() terlebih dahulu. Fungsi str() digunakan untuk
# mengkonversi segala jenis data ke bentuk string.

text = "hello"
number = 123
yes = True

message = text + " " + str(number) + " " + str(yes)
print(message)

#Menggunakan method join() milik string.

text = " ".join(["hello", "python"])
print(text)