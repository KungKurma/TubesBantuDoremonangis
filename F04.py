# Program Pencarian Gadget Berdasarkan Tahun Ditemukan

# Mencari gadget berdasarkan tahun ditemukan
# I.S. Menerima database gadget, input tahun, dan kategori pencarian (asumsi input valid)
# F.S. Mencetak hasil pencarian


# KAMUS 
# tahun : integer
# kategori : string
# found : boolean


# FUNGSI DAN PROSEDUR

def cetakSearch(Id, database):
# Prosedur mencetak info gadget Id

# KAMUS LOKAL

# ALGORITMA
    print("Nama: ", database[Id][1])
    print("Deskripsi: ", database[Id][2])
    print("Jumlah: ", database[Id][3])
    print("Rarirty: ", database[Id][4])
    print("Tahun Ditemukan: ", database[Id][5])


# PROGRAM UTAMA
def cariGadget(database):
    # Meminta input user
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")

    found = False

    print("\nHasil Pencarian :\n")

    # Pengeceakan dan pencetakan hasil pencarian
    if (kategori == "="):
        for i in database:
            if i[5] == tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == ">"):
        for i in database:
            if i[5] > tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == "<"):
        for i in database:
            if i[5] < tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == ">="):
        for i in database:
            if i[5] >= tahun:
                found = True
                cetakSearch(i, database)

    else: # kategori == "<="
        for i in database:
            if i[5] <= tahun:
                found = True
                cetakSearch(i, database)
    
    # Hasil cetak bila tidak ditemukan gadget sesuai dengan kategori pencarian
    if not(found):
        print("Tidak ada gadget yang ditemukan")