fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

#Tersedia juga method intersection_update() yang berguna untuk mengubah nilai data (dimana method dipanggil)
# dengan nilai baru yang didapat dari kesamaan elemen antara data tersebut vs. data pada argument pemanggilan method.

fellowship.intersection_update(hobbits)
print("fellowship:", fellowship)