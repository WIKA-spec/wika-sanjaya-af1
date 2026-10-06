seq = []
for i in range(10):
    if i % 2 == 1: seq.append(i)
    print(seq)

#bisa dituliskan lebih ringkas menjadi seperti berikut:
seq = [i for i in range(10) if i % 2 == 1]
print(seq)