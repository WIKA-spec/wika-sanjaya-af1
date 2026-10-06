fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

diff = fellowship.difference(hobbits)
print("diff:", diff)

#Selain method di atas, adalagi method difference_update() yang kegunaannya adalah mengubah nilai data
# (dimana method dipanggil) dengan nilai baru yang didapat dari perbedaan elemen antara data tersebut vs. data pada argument pemanggilan method.

fellowship.difference_update(hobbits)
print("fellowship:", fellowship)