print  ("Selamat datang di Program Biodata ")
print ("=================================")

# Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks
print ("==============================")
teks = "Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat)

# buka file untuk ditulis
tulis_bio = open("biodata.txt", "a")

# tulis teks ke file
tulis_bio.write(teks)

# tutup file
tulis_bio.close()