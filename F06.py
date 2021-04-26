# Program Menghapus Item

# I.S. Menerima input ID barang yang akan dibuang (diperiksa apakah barang itu ada)
# F.S. Item dibuang dari database


# KAMUS 
# databaseG : list of list
# databaseC : list of list

# ID : string


# FUNGSI DAN PROSEDUR

def searchDatabase(Id, database):
# Fungsi yang memeriksa apakah sebuah Id ada di dalam database

# KAMUS LOKAL
# found : boolean

# ALGORITMA
    found = False   # Variable yang menyimpan apakah ID ada di database

    for i in database:

        if i[0] == Id:
            found = True
            break

    return found


def searchDatabase(ID, database):
# Fungsi yang memeriksa apakah sebuah Id ada di dalam database

# KAMUS LOKAL
# found : boolean

# ALGORITMA
    found = False   # Variable yang menyimpan apakah ID ada di database

    for i in database:

        if i[0] == ID:
            found = True
            break

    return found


def getIndex(ID, database):
# Fungsi mendapatkan index suatu item di database berdasarkan ID (asumsi ID memang ada di database)

# KAMUS LOKAL

# ALGORITMA
    for i in range(len(database)):
        if database[i][0] == ID:
            return i


def removeDatabase(ID, database):
# Prosedur yang dijalankan program setelah validasi (asumsi ID memang ada di database)

# KAMUS LOKAL
# index : integer
# nama : string
# confirmation : string
# temp: list of list

# ALGORITMA
    index = getIndex(ID, database)  # Index dari item
    nama = database[index][1]   # Nama dari item
    confirmation = ""

    while True:
        confirmation = input("Apakah anda yakin ingin menghapus " + nama + " (Y/N)? ")
        
        if (confirmation == "N"):   # Jika user tidak jadi menghapus
            print("\nPenghapusan dibatalkan.")
            return database # Terminasi

        elif (confirmation == "Y"): # Jika user jadi menghapus

            # Kode penghapusan dengan index 
            temp = database[:index] 
            for i in database[(index + 1):]:
                temp.append(i)
            database = temp

            print("\nItem telah berhasil dihapus dari database")
            return database # Terminasi
        
        else:   # Pesan error dan input diulang
            print("\nInput tidak valid. Masukkan lagi!")
    


# PROGRAM UTAMA
def hapusItem(databaseG, databaseC):

    # Input ID
    ID = input("Masukan ID: ")
    
    # Pengecekan ID ada di database
    if not(searchDatabase(ID, databaseG)) and not(searchDatabase(ID, databaseC)):    # Bila ID tidak ada di kedua database
        print("\nTidak ada item dengan ID tersebut")
        return (databaseG, databaseC)   # Terminasi

    else:
        if ID[0] == "G":
            databaseG = removeDatabase(ID, databaseG)
        else: # Bila ID untuk consumable
            databaseC = removeDatabase(ID, databaseC)

        return (databaseG, databaseC)   # Terminasi
        



    
        



dumG = [ ["G1","Parametric Transformer","Sering dilupakan",10,'A',2020],
         ["G2","Iphone 20","Layarnya 40 inchi",2,'B',2054],
         ["G3","Swrirly Chair","You spin me right round, baby, right round like a record baby, right round, rpund, round.",3,'C',1776],
         ["G4","Stand Arrow","*insert any jojo meme*",3,'S',1987],
         ["G5","Handphone Nokia","Benda terkuat di dunia",100,'B',2005],
         ["G6","Go Go Gadget: Oil Slick","Prone to slip ups and combustion",2,'C',1989],
         ["G8","SUPERSEMAR","Lah, kok di sini?",1,'S',1996]]

dumC = [ ["C1","Parametric Transformer","Sering dilupakan",10,'A'],
         ["C2","Iphone 20","Layarnya 40 inchi",2,'B'],
         ["C3","Swrirly Chair","You spin me right round, baby, right round like a record baby, right round, rpund, round.",3,'C'],
         ["C4","Stand Arrow","*insert any jojo meme*",3,'S'],
         ["C5","Handphone Nokia","Benda terkuat di dunia",100,'B'],
         ["C6","Go Go Gadget: Oil Slick","Prone to slip ups and combustion",2,'C'],
         ["C8","SUPERSEMAR","Lah, kok di sini?",1,'S'] ]
