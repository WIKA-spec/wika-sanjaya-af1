seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))
print(seq)

#bisa dijadikan lebih ringkas lagi menggunakan list comprehension:
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]
print(seq)