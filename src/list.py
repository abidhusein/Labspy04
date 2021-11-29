list_saya = ["Mangga", "Jeruk", "Pisang", "Jambu", "Rambutan"]

print ("Menampilakan Elemen ke 3")
print (list_saya[2])
print ()
print ("Menampilkan elemen ke 2 sampai elemen 4")
print (list_saya[1:4])
print ()
print ("Menampilkan elemen terakhir")
print (list_saya[-1])
print ()

print ("Mengubah elemen 4 dengan elemen lain")
list_saya[3] = "Nangka"
print (list_saya[3])
print ()

print ("Mengubah elemen 4 sampai elemen terakhir")
list_saya[3:4] = ["semangka","alpukat"]
print (list_saya[3:-1])
print ()


print ("Mengambil 2 bagian dari list")
b = list_saya[0:1]
print (b)
print ()

print ("Menambahkan Nilai")
b.append("Nanas")
print (b)
print ()

print ("Menambahkan 3 nilai")
b.extend([1,2,3])
print (b)
print ()

print ("Menggabungkan list A dan B")
c = list_saya + b
print (c)
