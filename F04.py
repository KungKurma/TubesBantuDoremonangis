# Program Pencarian Gadget Berdasarkan Tahun Ditemukan

# Mencari gadget berdasarkan tahun ditemukan
# I.S. Menerima database gadget, input tahun, dan kategori pencarian (asumsi input valid)
# F.S. Mencetak hasil pencarian


# KAMUS 
# database : list of list
# tahun : integer
# kategori : string
# found : boolean
# panjang : integer


# FUNGSI DAN PROSEDUR

def cetakSearch(Id, database):
# Prosedur mencetak info gadget Id

# KAMUS LOKAL

# ALGORITMA
    print("Nama: ", database[Id][1])
    print("Deskripsi: ", database[Id][2]    )
    print("Jumlah: ", database[Id][3])
    print("Rarirty: ", database[Id][4])
    print("Tahun Ditemukan: ", database[Id][5])
    print("")


# PROGRAM UTAMA
def cariGadget(database):
    # Meminta input user
    tahun = int(input("\nMasukkan tahun: "))
    kategori = input("Masukkan kategori: ")

    found = False
    panjang = len(database)

    print("\nHasil Pencarian :\n")

    # Pengeceakan dan pencetakan hasil pencarian
    if (kategori == "="):
        for i in range(panjang):
            if database[i][5] == tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == ">"):
        for i in range(panjang):
            if database[i][5] > tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == "<"):
        for i in range(panjang):
            if database[i][5] < tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == ">="):
        for i in range(panjang):
            if database[i][5] >= tahun:
                found = True
                cetakSearch(i, database)

    else: # kategori == "<="
        for i in range(panjang):
            if database[i][5] <= tahun:
                found = True
                cetakSearch(i, database)
    
    # Hasil cetak bila tidak ditemukan gadget sesuai dengan kategori pencarian
    if not(found):
        print("Tidak ada gadget yang ditemukan")

"""
Nanti ini hapus

dummyList = [ ["G1","Parametric Transformer","Sering dilupakan",10,'A',2020],
              ["G2","Iphone 20","Layarnya 40 inchi",2,'B',2054],
              ["G3","Swrirly Chair","You spin me right round, baby, right round like a record baby, right round, rpund, round.",3,'C',1776],
              ["G4","Stand Arrow","*insert any jojo meme*",3,'S',1987],
              ["G5","Handphone Nokia","Benda terkuat di dunia",100,'B',2005],
              ["G6","Go Go Gadget: Oil Slick","Prone to slip ups and combustion",2,'C',1989],
              ["G6","SUPERSEMAR","Lah, kok di sini?",1,'S',1996] ]

"""