seq = []
for i in range(5):
    seq.append(i * 2)
    print(seq)

#bisa dituliskan lebih ringkas menggunakan list comprehension, menjadiseperti berikut:
seq = [i * 2 for i in range(5)]
print(seq)